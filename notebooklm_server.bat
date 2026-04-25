@echo off
echo ============================================
echo  NotebookLM MCP Server - Servidor Bridge
echo ============================================
echo.
echo Iniciando servidor MCP en modo HTTP (puerto 8765)...
echo No cierres esta ventana mientras uses Antigravity.
echo.
python -m uv tool run --from notebooklm-skill notebooklm-mcp --http --port 8765
