release: python manage.py migrate
web: daphne backend.asgi:application
worker: python manage.py runworker channels --settings=backend.settings 
