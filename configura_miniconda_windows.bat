echo "Instalando miniconda"
call curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
call start /wait "" .\miniconda.exe /S
call del .\miniconda.exe
