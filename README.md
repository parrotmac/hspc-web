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
- DATABASE=postgres               # Use as PostgreSQL backend
- POSTGRES_HOST=postgres          # Hostname of Postgres database
- POSTGRES_PORT=5432              # DB Port
- POSTGRES_PASSWORD=password123!  # DB Password
- DJANGO_SECRET_KEY=<random data> # Secret key for Django to use (see https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
- DJANGO_ENV=[PRODUCTION|DEBUG]   # If set to PRODUCTION Django's DEBUG settings will be False. Defaults to True
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

Copyright 2017 Health Services Platform Consortium

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
