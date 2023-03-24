import pytest

from utils import request_table, assert_table, load_templates

templates = load_templates('sec')


@pytest.mark.parametrize('template', templates)
def test(template):
    table = request_table(template)
    assert_table(template, table)
