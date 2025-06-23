import asyncio
from playwright.async_api import async_playwright

async def get_pinnacle_data():
    url = "https://www.pinnacle.com/en/odds/match/football"
    print("🔗 Sayta daxil olunur...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, timeout=60000)

        await page.wait_for_timeout(5000)  # 5 saniyəlik gözləmə (test məqsədli)

        content = await page.content()
        print("✅ HTML alındı:")
        print(content[:1000])  # Yalnız ilk 1000 simvolu göstərir

        await browser.close()

asyncio.run(get_pinnacle_data())
