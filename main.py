import asyncio
from playwright.async_api import async_playwright

async def run_scraper():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # headless rejimi aktivdir
        page = await browser.new_page()

        print("Sayta daxil olunur...")
        await page.goto("https://www.bet365.com", timeout=60000)

        await page.wait_for_timeout(10000)  # 10 saniyə gözlə

        # HTML çıxarışı — bu mərhələdə sadəcə əsas səhifəni çap edir
        content = await page.content()
        print("HTML alınan hissə:\n")
        print(content[:3000])  # ilk 3000 simvolu göstər

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_scraper())
