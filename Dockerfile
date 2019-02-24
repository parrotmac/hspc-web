FROM node:8-alpine as builder

RUN mkdir -p /app/build
WORKDIR /app/build

COPY package.json /app/build/

RUN npm install

COPY . /app/build/

RUN npm run build

FROM python:3.7
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /django

WORKDIR /django

COPY requirements.txt /django/requirements.txt

RUN pip install -r requirements.txt

COPY hspc_home /django/hspc_home
COPY templates /django/templates
COPY website /django/website
COPY manage.py /django/
COPY upgrade-and-run.sh /django/

COPY --from=builder /app/build/website/static/styles/ /django/website/static/styles/

RUN python manage.py collectstatic --noinput --clear

ENTRYPOINT ["/django/upgrade-and-run.sh"]
