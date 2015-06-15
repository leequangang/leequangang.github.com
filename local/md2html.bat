@echo off
@echo 该脚本生成网络依赖版html文件！
echo.

set /p var=请输入md文件名(可连续输入多个文件):

python .\src\md2html.py %var%

pause