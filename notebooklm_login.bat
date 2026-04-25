@echo off
echo ============================================
echo  NotebookLM MCP Bridge - INICIO DE SESION
echo ============================================
echo.
echo Se abrira Chrome para que inicies sesion con tu cuenta de Google.
echo Inicia sesion y luego cierra el navegador.
echo.
python -m uv tool run --from notebooklm-skill notebooklm login
echo.
echo ============================================
echo  Login completado. Sesion guardada.
echo ============================================
pause
