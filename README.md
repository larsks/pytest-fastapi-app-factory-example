This repository accompanies [this stack overflow answer](https://stackoverflow.com/a/76637496/147356).

Create a virtual environment:

```
python -m venv .venv
```

Activate the virtual environment:

```
. .venv/bin/activate
```

Install the requirements:

```
pip install -r requirements.txt -r test-requirements.txt
```

Run the tests:

```
pytest -v
```
