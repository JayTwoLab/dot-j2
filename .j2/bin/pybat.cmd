@echo off
:: Check if J2_ROOT is defined
if "%J2_ROOT%"=="" (
    echo [Error] J2_ROOT environment variable is not set.
    echo Please run 'env.bat' first.
    exit /b 1
)

:: Path to the core python script
set "PYBAT_CORE=%J2_ROOT%\python\pybat.py"

:: Check if the core script exists
if not exist "%PYBAT_CORE%" (
    echo [Error] pybat.py not found at: %PYBAT_CORE%
    exit /b 1
)

:: Execute the script with all passed arguments
python "%PYBAT_CORE%" %*
