python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
