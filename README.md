# Barcode Generator

This project was developed using Python during NLW 2024 event from Rocketseat.

## Techs
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Python](https://www.python.org/doc/)
- [python-barcode](https://pypi.org/project/python-barcode/)
- [cerberus](https://pypi.org/project/Cerberus/)
- [pytest](https://pypi.org/project/pytest/)

## Overview
A single POST route was made using Flask ("/create_tag") to provide the functionality of creating tags for barcode. Python Barcode lib was used to handle this barcode generation and Cerberus for body validation schemas. Pytest was used to create unit tests for the use case.

I've tried using Clean Code principles for building highly scalable and mantainable software acrchitecture:
- main: contains the core application like the server and routes
- views: handle the HTTP layer
- controllers: contains the entities with the business logic
- drivers: contains the external libs like barcode handler
- errors: the handler for exceptions
- validators: the validation schemas for requests using Cerberus

## How to run
### Virtual environment
- Create a virtual environment and install the dependencies.

- #### Using pipenv
  If you don't have pipenv installed, check the docs: https://pipenv.pypa.io/en/latest/

```python

# using pipenv
pipenv install

# activate virtual env
pipenv shell

```

- #### Using virtualenv

```python

# using virtualenv
pip install virtualenv
python -m venv .venv

# active virtual env (for Unix/MacOS)
source venv/bin/activate

# active virtual env (for Windows)
.venv\Scripts\activate

# install the deps
pip install -r requirements.txt

```

### Run the project
  The project will run on http://localhost:3000/

```python

# using pipenv
pipenv run run.py

# using virtualvenv
python run run.py

```

### Create a barcode
  You can use any API platform to test it.
  Endpoint: http://localhost:3000/create_tag

#### REQUEST BODY
```json
{
  "product_code": "123456"
}

```

#### RESPONSE 200 (Success)
```json
{
	"data": {
		"count": 1,
		"path": "123456.png",
		"type": "Tag Image"
	}
}

```

#### RESPONSE 422 (Unprocessable Entity)

##### Request Body
```json
{
  "mock_unexistent_field": "123456"
}
```
##### Response
```json
{
	"errors": [
		{
			"detail": {
				"mock_unexistent_field": [
					"unknown field"
				],
				"product_code": [
					"required field"
				]
			},
			"name": "Unprocessable Entity"
		}
	]
}

```

If success, a .png file with the generated barcode will be created in ./src.

### Run unit tests
```python
pytest
```
