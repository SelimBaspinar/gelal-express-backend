release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: daphne backend.asgi:application --port  $PORT -bind 0.0.0.0 -p
chatworker: python manage.py runworker --settings=backend.settings
