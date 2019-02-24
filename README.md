# HSPC Website
HSPConsortium Website

[![Build Status](https://travis-ci.org/parrotmac/hspc-web.svg?branch=master)](https://travis-ci.org/parrotmac/hspc-web)

### Requirements
- Python >= 3.5
- pip
- node/npm (tested with node 8.x)
- (optionally) Docker >= 17.0.5

### Supported Environmental Variables
_Note: The project will default to SQLite if `DATABASE` is not specified_
```
- DATABASE=postgres      # Use PostgreSQL. Yeah!
- POSTGRES_HOST          # Hostname of Postgres cluster. Default: localhost
- POSTGRES_PORT          # The network port. Default: 5432
- POSTGRES_USER          # User for database connections. Default: www
- POSTGRES_PASSWORD      # No default is set.
- POSTGRES_SCHEMA        # The Postgres database name. Default: www_development

- DJANGO_SECRET_KEY      # Defaults to a random string. The secret key for Django to use (see https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
- DJANGO_ENV=[PRODUCTION|DEBUG]   # If set to PRODUCTION or True, Django's DEBUG settings will be False. Default: True

- AWS_STORAGE_BUCKET_NAME   # Name of S3 bucket
- AWS_ACCESS_KEY_ID         # Access key for resource
- AWS_SECRET_ACCESS_KEY     # Secret access key for resource
- AWS_S3_CUSTOM_DOMAIN      # Optional. Useful if using a S3-like provider other than AWS. Default: '<AWS_STORAGE_BUCKET_NAME>.s3.amazonaws.com'
```
### Development/Local machine

_First time setup_
```
git clone https://github.com/parrotmac/hspc-web
cd hspc-web
pip install -r requirements.txt
npm install
```

_Run the project_
```
npm run dev
```

### Using Docker

**Prebuilt image:** [`https://hub.docker.com/r/isaacp/hspc-django/`](https://hub.docker.com/r/isaacp/hspc-django/)

**Run:** _Use `docker-compose` (see included `docker-compose.yml`)_

**Build:**
```
docker build -t hspc-django .
```

# License

Copyright 2019 Isaac Parker, unless otherwise noted

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
