flask db migrate -m "commit"
flask db upgrade
pip freeze > requirements.txt
pip install -r requirements.txt