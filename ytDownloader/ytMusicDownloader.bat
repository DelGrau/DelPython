@echo off 
title Baixar Musica 
set /p LINK="Link do Video: "
python C:\Programas\Python\python_Projects\ytDownloader\ytMusicDownloader.py %LINK%
pause