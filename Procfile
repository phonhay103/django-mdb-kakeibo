release: python manage.py migrate && python manage.py loaddata initial.json
web: gunicorn project.wsgi --log-file -