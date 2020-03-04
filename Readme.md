# Universe Django Tutorial

## Getting started
in the project root create new virtualenv, install dependencies and do the migrations

for example
```bash
python3 -m venv djangoenv
source djangoenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Running the server
```bash
python manage.py runserver
```

## Accessing admin-panel when server is running
First create superuser with
```bash
python manage.py createsuperuser
```
Then you can access the admin panel from localhost:8000/admin