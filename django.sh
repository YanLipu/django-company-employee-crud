#!/bin/bash
echo "Create migrations"
python manage.py makemigrations core
echo "=================================="

echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Seeding superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('joseyan', 'jose@yan.com', 'admin123')" | python manage.py shell
echo "=================================="

echo "Seeding regular user"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_user('messi', 'messi@yan.com', 'senha123')" | python manage.py shell
echo "=================================="

echo "Start server"
python manage.py runserver 0.0.0.0:8000