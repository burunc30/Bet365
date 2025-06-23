import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth

async def main():
    print("Playwright işə salınır...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # istəsən headless=False et
        context = await browser.new_context()
        page = await context.new_page()

        # Stealth aktivləşdirilir
        await stealth(page)

        print("Sayta daxil olunur...")
        await page.goto("https://www.878365.com/", timeout=60000)
        await page.wait_for_timeout(3000)  # 3 saniyə gözlə (lazımdırsa)

        # HTML çıxarılır
        html = await page.content()
        print("HTML alınan hissə:")
        print(html[:1000])  # çox uzun olmasın deyə ilk 1000 simvolu göstərir

        await browser.close()

# Əsas funksiyanı işə sal
if __name__ == "__main__":
    asyncio.run(main())
