@echo off
@echo �ýű���������������html�ļ���
echo.

set /p var=������md�ļ���(�������������ļ�):

python .\src\md2html.py %var%

pause