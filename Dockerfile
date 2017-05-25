FROM python:3.6
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /django

WORKDIR /django

COPY requirements.txt /django/requirements.txt

RUN pip install -r requirements.txt

COPY . /django/

RUN mkdir -p /django/static/

RUN python manage.py collectstatic --noinput --clear

ENTRYPOINT ["/usr/local/bin/gunicorn", "hspc_home.wsgi:application", "-w 2", "-b :8000"]