@echo off
title Iniciando Aplicacao
color 0A
echo.
echo ================================================
echo   Iniciando com Poetry
echo ================================================
echo.

REM Verificar Poetry
where poetry >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERRO: Poetry nao encontrado!
    pause
    exit /b 1
)

REM Instalar se necessário
if not exist ".venv\Scripts\activate.bat" (
    echo Instalando dependencias...
    poetry install
)

REM Instalar frontend
if not exist "app\frontend\node_modules" (
    echo Instalando frontend...
    cd app\frontend
    call npm install
    cd ..\..
)

echo Iniciando servicos...
echo.

REM Backend
start "Backend - Port 5000" cmd /k "poetry run uvicorn app.backend.main:app --host 0.0.0.0 --port 5000 --reload"

timeout /t 3 /nobreak >nul

REM Frontend
start "Frontend - Port 4200" cmd /k "cd /d %~dp0\app\frontend && npm start"

echo.
echo ================================================
echo   Servicos Iniciados!
echo ================================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:4200
echo Docs:     http://localhost:5000/docs
echo.
pause