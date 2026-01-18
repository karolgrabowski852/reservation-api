#!/bin/bash
set -ex
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations

python3 manage.py migrate

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'python'
email = 'python@example.com'
password = 'python'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"SUKCES: Superużytkownik '{username}' został utworzony.")
else:
    print(f"INFO: Użytkownik '{username}' już istnieje, pomijam.")
EOF

exec "$@"