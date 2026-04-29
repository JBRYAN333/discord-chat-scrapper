@echo off
REM Script para exportar mensagens do Discord usando DiscordChatExporter
REM
REM CONFIGURAÇÃO:
REM 1. Baixe o DiscordChatExporter CLI de: https://github.com/Tyrrrz/DiscordChatExporter/releases
REM 2. Extraia na mesma pasta deste script
REM 3. Configure as variáveis abaixo

REM ===== CONFIGURAÇÃO =====
SET TOKEN=SEU_TOKEN_AQUI
SET CHANNEL_ID=465332971369660419
SET DATA_INICIO=2025-03-11
SET DATA_FIM=2026-04-29
SET OUTPUT_DIR=../output

REM ===== EXECUÇÃO =====
echo Exportando mensagens do Discord...
echo Canal: %CHANNEL_ID%
echo Periodo: %DATA_INICIO% ate %DATA_FIM%
echo.

.\DiscordChatExporter.Cli export -t "%TOKEN%" -c %CHANNEL_ID% -f Json -o %OUTPUT_DIR% --after %DATA_INICIO% --before %DATA_FIM%

echo.
echo Exportacao concluida!
pause
