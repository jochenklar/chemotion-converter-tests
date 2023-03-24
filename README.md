chemotion-converter-tests
=========================

Setup
-----

```
pip install -r requirements.txt
```

The `files` directory is not part of this repo, it needs to be created with the following layout:

```
files
├── aif
├── ascii
├── asc_zip
├── brml
├── cary
├── cif
├── csv
├── dsp
├── dta
├── jasco
├── nova
├── pdf
├── pssession
├── sec
├── sem
├── xlsx
└── xy
```

Usage
-----

First, the [chemiotion-converter-app](https://github.com/ComPlat/chemotion-converter-app) needs to run at http://localhost:5000.

Then, the tests can be started with:

```
pytest                    # run all tests
pytest tests/test_csv.py  # run tests for a particular file type
```
