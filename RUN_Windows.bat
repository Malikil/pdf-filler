@echo off
pipenv run python src\gui.py

:: Pause only if the program generated an error
if %ERRORLEVEL% neq 0 goto ProcessError
exit /b 0

:ProcessError
pause
exit /b 1
