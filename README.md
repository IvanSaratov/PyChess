### README ###

Устанавливаем виртуальное окружение и сразу после запускаем его:

```
python -m venv venv/
venv/Scripts/activation
```

Устанавливаем нужные пакеты для работы программы из списка зависимостей:
```
pip install -r requirements.txt
```

Устанавливаем переменную окружения которой сообщаем где находится главный файл программы:
```
for Windows:
  set FLASK_APP=chess.py
for Linux:
  export FLASK_APP=chess.py
```
Создаем базу данных и после можем запускать программу
```
flask db upgrade
flask run
```
