import json

from pathlib import Path

import requests


def load_templates(name):
    template_path = Path('templates').joinpath(name).with_suffix('.json')
    return json.load(open(template_path))


def request_table(template):
    file_path = Path('files') / template['path']
    response = requests.post('http://localhost:5000/tables', files={'file': open(file_path, 'rb')})
    response.raise_for_status()
    return response.json()


def assert_table(template, table):
    for key, template_metadata in template.get('metadata', {}).items():
        table_metadata = table['metadata'].get(key)
        assert table_metadata == template_metadata, \
               f"{template['path']} -> fileMetadata -> {key} -> {table_metadata} != {template_metadata}"

    template_tables = template.get('tables')
    if template_tables:
        table_ntables = len(table['tables'])
        template_ntables = len(template_tables)
        assert table_ntables == template_ntables, (template['path'], 'ntables')

        for i, template_table in enumerate(template_tables):
            for key, template_metadata in template_table.get('metadata', {}).items():
                table_metadata = table['tables'][i]['metadata'].get(key)
                assert table_metadata == template_metadata, \
                       f"{template['path']} -> tableMetadata -> Table#{i} -> {key} -> {table_metadata} != {template_metadata}"

            template_columns = template_table.get('columns')
            if template_columns:
                for j, template_column in enumerate(template_columns):
                    table_column_name = table['tables'][i]['columns'][j].get('name')
                    if template_column is None:
                        template_column_name = f'Column #{j}'
                    else:
                        template_column_name = f'Column #{j} ({template_column})'
                    assert table_column_name == template_column_name, \
                           f"{template['path']} -> columnName -> {table_column_name} != {template_column_name}"
