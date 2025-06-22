import asyncio
from playwright.async_api import async_playwright

async def scrape_bet365():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print("Sayta daxil olunur...")
        await page.goto("https://www.878365.com/#/AC/B1/C1/D13/E2/F16/", timeout=60000)

        await page.wait_for_timeout(10000)  # Sayfanın yüklənməsini gözləyirik

        content = await page.content()
        print("Səhifə məzmunu alındı.")
        
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(content)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_bet365())
