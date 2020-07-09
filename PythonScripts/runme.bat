@echo off

FOR /F "tokens=*" %%a in ('dir /b *.ma') do SET MAYA=%%a
FOR /F "tokens=*" %%a in ('dir /b *.csv') do SET CSV=%%a

cmd /k "pip install virtualenv & virtualenv venv & cd /d venv\Scripts & activate & cd /d  ../.. & pip install -r requirements.txt & python Rename.py %MAYA% %CSV% runserver & deactivate"