FROM node:8-alpine

RUN apk update
RUN apk add alpine-sdk
RUN apk add ruby ruby-dev ruby-rdoc ruby-irb
RUN apk add libffi-dev

RUN gem install sass

RUN mkdir -p /app/build
WORKDIR /app/build

COPY package.json /app/build/

RUN npm install

COPY Gruntfile.js /app/build/

COPY . /app/build/

RUN npm run build

RUN rm -rf website/static

#FROM python:3.6
#ENV PYTHONUNBUFFERED 1
#
#EXPOSE 8000
#
#RUN mkdir /django
#
#WORKDIR /django
#
#COPY requirements.txt /django/requirements.txt
#
#RUN pip install -r requirements.txt
#
#COPY . /django/
#
#RUN mkdir -p /django/static/
#
#RUN python manage.py collectstatic --noinput --clear
#
#ENTRYPOINT ["/django/upgrade-and-run.sh"]
