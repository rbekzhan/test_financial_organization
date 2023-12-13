#!/bin/sh

python manage.py migrate --no-input

python manage.py collectstatic --no-input

python manage.py populate_data

uwsgi --http 0.0.0.0:8000 --module core.wsgi:application