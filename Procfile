release: python manage.py migrate
web: gunicorn backend.wsgi:application
web: daphne core.asgi:application --port $PORT --bind 0.0.0.0
worker: python manage.py runworker channels --settings=backend.settings 
