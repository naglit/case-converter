SET mypath=%~dp0
echo %mypath:~0,-1%

cd %mypath:~0,-1%\src
rename sample.txt files.txt