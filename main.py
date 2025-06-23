import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def main():
    print("🔗 Sayta daxil olunur...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.pinnacle.com/en/odds/match/soccer")  # Saytın əsas əmsal səhifəsi
        await page.wait_for_timeout(8000)  # 8 saniyə gözləyək ki, tam yüklənsin

        content = await page.content()
        print("✅ HTML alındı.")

        # HTML-i BeautifulSoup ilə emal edirik
        soup = BeautifulSoup(content, "html.parser")

        matches = soup.find_all("div", class_="style_row__e1n46")  # Match blokları

        for match in matches:
            try:
                teams = match.find_all("span", class_="style_teamName__3xR9D")
                if len(teams) != 2:
                    continue
                home = teams[0].get_text(strip=True)
                away = teams[1].get_text(strip=True)

                odds = match.find_all("span", class_="style_price__f4CXD")
                if len(odds) < 3:
                    continue
                odd_1 = odds[0].get_text(strip=True)
                odd_x = odds[1].get_text(strip=True)
                odd_2 = odds[2].get_text(strip=True)

                print(f"{home} vs {away} | 1: {odd_1} | X: {odd_x} | 2: {odd_2}")

            except Exception as e:
                print("Xəta oldu:", e)

        await browser.close()

asyncio.run(main())
