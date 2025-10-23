@echo off
title Parando Aplicacao
color 0C
echo.
echo ================================================
echo   Parando Frontend e Backend
echo ================================================
echo.

echo Procurando processos do Backend (porta 5000)...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":5000" ^| find "LISTENING"') do (
    echo Matando processo %%a
    taskkill /F /PID %%a >nul 2>&1
)

echo.
echo Procurando processos do Frontend (porta 4200)...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":4200" ^| find "LISTENING"') do (
    echo Matando processo %%a
    taskkill /F /PID %%a >nul 2>&1
)

echo.
echo Procurando processos node.exe e python.exe...
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1

echo.
echo ================================================
echo   Servicos Parados com Sucesso!
echo ================================================
echo.
pause