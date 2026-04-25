import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        print("Navigating to local server...")
        await page.goto("http://localhost:5173/Portafolio/")
        await page.wait_for_timeout(2000)
        
        print("Clicking APRENDE TYBA...")
        await page.click("#nav-tyba")
        await page.wait_for_timeout(2000)
        
        print("Taking screenshot of layout...")
        await page.screenshot(path="screenshot_layout.png")
        
        print("Clicking VER VIDEO...")
        await page.click("text=VER VIDEO")
        await page.wait_for_timeout(2000)
        
        print("Taking screenshot of overlay...")
        await page.screenshot(path="screenshot_overlay.png")
        
        await browser.close()

asyncio.run(main())
