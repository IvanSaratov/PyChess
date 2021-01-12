### README ###

python -m venv venv/
venv/Scripts/activation
pip install -r requirements.txt

for Windows:
  set FLASK_APP=chess.py
for Linux:
  export FLASK_APP=chess.py

flask db upgrade
flask run