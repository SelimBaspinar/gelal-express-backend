release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: daphne -b 0.0.0.0 -p 8001 backend.asgi:application
chatworker: python manage.py runworker --settings=backend.settings
