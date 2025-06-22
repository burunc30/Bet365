import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Sayta daxil olunur...")
    url = "https://www.878365.com"  # Mirror domain
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, timeout=60000)
        content = await page.content()
        print("HTML alınan hissə:")
        print(content[:2000])  # ilk 2000 simvol göstərilir
        await browser.close()

asyncio.run(main())
