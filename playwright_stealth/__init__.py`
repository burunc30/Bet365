import asyncio

async def stealth_async(page):
    await page.add_init_script(path="stealth.js")

def stealth_sync(page):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(stealth_async(page))
