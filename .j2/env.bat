@echo off

:: current \.j2 directory 
set "J2_ROOT=%CD%"

if not exist "%J2_ROOT%" (
    echo [Warning] .j2 folder not found in the current directory.
)

set "PATH=%J2_ROOT%\bin;%J2_ROOT%\lib;%PATH%"

:: Add platform-specific paths
if exist "%J2_ROOT%\bin\win" (
    set "PATH=%J2_ROOT%\bin\win;%PATH%"
)

echo J2 Environment Activated.
echo J2_ROOT is set to: %J2_ROOT%


