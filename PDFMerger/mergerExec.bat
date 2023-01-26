@echo off
title PDF Merger

:check
if exist ./PDF/arquivo.pdf (goto delArquivo) else (goto execMerge)

:delArquivo
del /Q .\PDF\arquivo.pdf
goto check

:execMerge
python ./PDFmerger.py

echo Operacao Concluida

pause