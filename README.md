# Instahyre-Contact-App

To run on your local machine:

one-time configurations:
python_version = 3.11.4
set virtual environment
enter command:
pip install -r requirements.txt

configure database in main.settings
python manage.py makemigrations home
python manage.py makemigrations contact
python manage.py makemigrations
python manage.py migrate

to run the app:
python manage.py runserver
