import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    user_data_dir = os.path.expanduser('~/.notebooklm/browser_profile')
    storage_state_path = os.path.expanduser('~/.notebooklm/storage_state.json')
    
    print(f"Abriendo navegador con perfil en: {user_data_dir}")
    print("POR FAVOR: Inicia sesión en la ventana que se abrirá.")
    print("Cuando veas tus libretas de NotebookLM, cierra la ventana del navegador.")
    
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            channel="chrome", # Usar tu Chrome real instalado
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
                "--excludeSwitches=enable-automation",
                "--use-fake-ui-for-media-stream",
            ],
            ignore_default_args=["--enable-automation"]
        )
        
        page = await context.new_page()
        await page.goto("https://notebooklm.google.com/")
        
        print("\nEsperando a que cierres el navegador para guardar la sesión...")
        
        # Keep the script running and save periodically
        while True:
            try:
                if not context.pages:
                    break
                # Save state while it's still open
                await context.storage_state(path=storage_state_path)
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Error guardando estado: {e}")
                break
        await context.close()
        print("\n¡LISTO! La sesión ha sido guardada de forma permanente.")

if __name__ == "__main__":
    asyncio.run(run())
