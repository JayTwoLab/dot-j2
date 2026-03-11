@echo off
:: Check if J2_ROOT is defined
if "%J2_ROOT%"=="" (
    echo [Error] J2_ROOT environment variable is not set.
    echo Please run 'env.bat' first.
    exit /b 1
)

:: Path to the core python script
set "PROCESS_MONITOR=%J2_ROOT%\python\process_monitor.py"

:: Check if the core script exists
if not exist "%PROCESS_MONITOR%" (
    echo [Error] process_monitor.py not found at: %PROCESS_MONITOR%
    exit /b 1
)

:: Execute the script with all passed arguments
python "%PROCESS_MONITOR%" %*
