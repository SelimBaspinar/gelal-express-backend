release: python manage.py migrate
web: gunicorn backend.wsgi:application
web: daphne backend.asgi:application
worker: python manage.py runworker channels --settings=backend.settings 
