release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
web: daphne -b 0.0.0.0 -p $PORT backend.asgi:application -v2
chatworker: python manage.py runworker --settings=backend.settings -v2
