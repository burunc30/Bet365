import asyncio
from playwright.async_api import async_playwright
import playwright_stealth

async def main():
    print("Playwright işə salınır...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Stealth modulunun içindəki funksiyanı ayrıca çağırırıq
        await playwright_stealth.stealth_async(page)

        print("Sayta daxil olunur...")
        await page.goto("https://www.878365.com/", timeout=60000)
        await page.wait_for_timeout(3000)

        html = await page.content()
        print("HTML alınan hissə:")
        print(html[:1000])  # çox uzun olmasın deyə

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
