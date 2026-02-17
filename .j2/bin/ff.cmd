@echo off
REM ff.cmd - Find files or directories in Windows using cmd
REM Usage: ff.cmd [-d|-f] <directory> <regex>
REM   -d: search directories only
REM   -f: search files only (default)
REM   <regex>: regular expression for file/directory name (case-insensitive)

setlocal enabledelayedexpansion

set "find_type=f"
set "args="

:parse_args
if "%1"=="-d" (
  set "find_type=d"
  shift
  goto parse_args
) else if "%1"=="-f" (
  set "find_type=f"
  shift
  goto parse_args
)

if "%3" NEQ "" (
  echo Usage: ff.cmd [-d|-f] ^<directory^> ^<regex^>
  exit /b 1
)

set "dir=%1"
set "regex=%2"

if "%dir%"=="" (
  echo Usage: ff.cmd [-d|-f] ^<directory^> ^<regex^>
  exit /b 1
)

REM Use PowerShell for regex matching and advanced find
if "%find_type%"=="d" (
  powershell -Command "Get-ChildItem -Path '%dir%' -Recurse -Directory | Where-Object { $_.Name -match '%regex%' } | ForEach-Object { $_.FullName }"
) else (
  powershell -Command "Get-ChildItem -Path '%dir%' -Recurse -File | Where-Object { $_.Name -match '%regex%' } | ForEach-Object { $_.FullName }"
)

endlocal
