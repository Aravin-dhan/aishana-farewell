import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 800, "height": 1800})
        await page.goto("file:///Users/Admin/GWIC/aishana-farewell/index.html")
        
        # Click the envelope to reveal the card
        await page.click("#envelope-wrapper")
        
        # Wait for card to appear
        await page.wait_for_selector(".scene-card.active", state="visible", timeout=5000)
        
        # Wait for animations to finish
        await page.wait_for_timeout(3000)
        
        # Grab the .invitation-card node exactly
        card = page.locator(".invitation-card")
        await card.screenshot(path="/Users/Admin/Desktop/GWIC_Farewell_Invite.png")
        
        await browser.close()

asyncio.run(main())
