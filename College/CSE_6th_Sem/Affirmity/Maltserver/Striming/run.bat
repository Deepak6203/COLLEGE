set FLASK_APP=app.py
set FLASK_ENV=development 
set PYTHONDONTWRITEBYTECODE=1
set FLASK_DEBUG=1

python -m flask run -p 5000


@REM @echo off

@REM set FLASK_APP=app.py
@REM set FLASK_ENV=development 
@REM set PYTHONDONTWRITEBYTECODE=1
@REM set FLASK_DEBUG=1

@REM gunicorn -w 4 -b 0.0.0.0:8000 app:app
