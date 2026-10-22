# Stack Overflow Clone — Django REST Framework

A Django project inspired by question-and-answer platforms, organized around accounts, questions, answers, and home pages. It includes Django REST Framework and API schema/documentation endpoints.

## Features visible in the project configuration
- Account, question, and answer apps
- Django REST Framework
- Token authentication package
- OpenAPI schema generation with drf-spectacular
- Swagger UI and ReDoc routes
- Django admin

## Stack
- Python and Django
- Django REST Framework
- DRF token authentication
- drf-spectacular

## Run locally
Create and activate a Python virtual environment, install the dependencies imported by the project, configure a private development secret key, and run:

```bash
python manage.py migrate
python manage.py runserver
```

## API documentation
The URL configuration exposes:
- `/schema/`
- `/schema/swagger-ui/`
- `/schema/redoc/`

The exact API routes are defined in each app's URL configuration.

## Security note
The current `drf/settings.py` still contains a hard-coded Django secret key. Replace it with a private `DJANGO_SECRET_KEY` environment variable and rotate the old value before using this project outside local development.
