#!/bin/bash
# make migrations first

python manage.py makemigrations

# Apply database migrations to database in container
echo "Apply database migrations"
python manage.py migrate

# Load Initial database data
python manage.py loaddata dumped_data

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:5000

