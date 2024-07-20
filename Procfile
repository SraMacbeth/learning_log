web: gunicorn learning_log.wsgi --config gunicorn.conf.py
post-deploy: python learning_log/management/commands/migrate_and_collect.py


