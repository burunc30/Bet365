import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from bs4 import BeautifulSoup

URL = "https://www.pinnacle.com/en/odds/match/football"

async def main():
    print("🔗 Sayta daxil olunur...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await stealth_async(page)  # Stealth tətbiq et
        await page.goto(URL, timeout=60000)
        html = await page.content()
        print("✅ HTML alındı.")

        soup = BeautifulSoup(html, "html.parser")

        # Sadə yoxlama üçün başlıq çıxarırıq
        title = soup.title.string if soup.title else "Başlıq yoxdur"
        print(f"🌐 Səhifə Başlığı: {title}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
