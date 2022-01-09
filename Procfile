release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: daphne -b 0.0.0.0 -p 8001 backend.asgi:application
worker: python manage.py runworker channels --settings=backend.settings -v2
