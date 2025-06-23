import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Sayta daxil olunur...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        page = await context.new_page()

        # Stealth.js faylını inject edirik
        with open("stealth.js", "r") as f:
            stealth_script = f.read()
        await page.add_init_script(stealth_script)

        # Burda mirror və ya əsas sayt fərq etməz — istədiyin domeni yoxlaya bilərik
        await page.goto("https://www.878365.com", timeout=60000)
        content = await page.content()
        print("HTML alınan hissə:\n", content[:1000])  # ilk 1000 simvol göstərək

        await browser.close()

asyncio.run(main())
