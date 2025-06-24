import asyncio
from playwright.async_api import async_playwright
import playwright_stealth

async def main():
    print("🔄 Playwright işə salınır...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Stealth tətbiq et
        await playwright_stealth.stealth_async(page)

        # 📌 Sayta keçid (Pinacle)
        url = "https://www.pinnacle.com/en/odds/match/football"
        print("🔗 Sayta daxil olunur...")
        await page.goto(url)

        # Sayta yüklenmesi üçün 5 saniyə gözləyirik
        await page.wait_for_timeout(5000)

        # HTML content-i əldə et və ilk 3000 simvolu göstər
        print("✅ Səhifə yükləndi, content alınır...")
        content = await page.content()
        print(content[:3000])

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
