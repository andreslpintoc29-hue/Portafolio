import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on("console", lambda msg: print(f"CONSOLE: {msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        print("Navigating to local server...")
        await page.goto("http://localhost:5173/Portafolio/")
        await page.wait_for_timeout(2000)
        
        print("Clicking APRENDE TYBA...")
        try:
            await page.click("#nav-tyba")
        except Exception as e:
            print("Failed to click APRENDE TYBA:", e)
            
        await page.wait_for_timeout(2000)
        
        print("Taking screenshot of layout...")
        await page.screenshot(path="screenshot_layout_reverted.png")
        
        await browser.close()

asyncio.run(main())
