import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=[
            "--disable-blink-features=AutomationControlled"
        ])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            locale="en-US",
            timezone_id="Europe/London"
        )
        page = await context.new_page()
        print("Sayta daxil olunur...")

        try:
            await page.goto("https://www.bet365.com", timeout=60000)
            await page.wait_for_timeout(10000)  # Cloudflare keçidini gözlə
            content = await page.content()

            # Fayla yaz
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(content)

            print("Səhifə uğurla yükləndi və yazıldı: page.html")

        except Exception as e:
            print("Xəta baş verdi:", e)

        await browser.close()

asyncio.run(main())
