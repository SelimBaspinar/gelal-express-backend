release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: daphne backend.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=backend.settings -v2
