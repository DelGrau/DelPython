@echo off 
title Baixar Video 
set /p LINK="Link do Video: "
python C:\Programas\Python\python_Projects\ytDownloader\ytDownloader.py %LINK%
pause