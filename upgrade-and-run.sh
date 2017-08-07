#!/bin/bash

/usr/bin/env python manage.py collectstatic --noinput --clear

/usr/bin/env python manage.py migrate

/usr/local/bin/gunicorn hspc_home.wsgi:application -w 2 -b :8000
