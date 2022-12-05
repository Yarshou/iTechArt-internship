python3 -m venv venv
. venv/bin/activate
touch requirements.txt;
pip3 install django
pip3 install psycopg2-binary
django-admin startproject core .
python3 manage.py startapp application