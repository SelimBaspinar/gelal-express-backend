release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
daphne -b 0.0.0.0 -p $PORT mysite.asgi:application
