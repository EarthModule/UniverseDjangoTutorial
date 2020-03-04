python3 -m venv djangovenv
source djangovenv/bin/activate
pip install Django
pip install django-admin
django-admin startproject universeproject
python manage.py migrate
python manage.py startapp starsystem