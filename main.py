import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

async def run():
    print("Sayta daxil olunur...")
    proxy = {
        "server": "http://138.201.5.75:3128",  # Test üçün açıq proxy
    }
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, proxy=proxy)
        context = await browser.new_context(user_agent=user_agent, java_script_enabled=True)
        page = await context.new_page()

        await stealth_async(page)  # Stealth modulu tətbiq edilir

        await page.goto("https://www.878365.com", timeout=60000)
        await page.wait_for_timeout(5000)

        content = await page.content()
        print("HTML alınan hissə:")
        print(content[:2000])  # İlk 2000 simvolu çap edir

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
