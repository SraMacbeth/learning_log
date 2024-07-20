web: gunicorn learning_log.wsgi --log-file -
post-deploy: python manage.py migrate && python manage.py collectstatic --noinput

