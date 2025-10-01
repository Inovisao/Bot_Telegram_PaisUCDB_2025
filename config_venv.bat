set "searchString=Python39"
set "python_path="

for /F "delims=" %%a in ('where python ^| findstr /c:"%searchString%"') do (
    set "python_path=%%a"
)
echo "%python_path%"

call %python_path% -m venv bot

call bot\Scripts\activate.bat

call bot\Scripts\python.exe -m pip install -r requirements.txt

echo "Feito"