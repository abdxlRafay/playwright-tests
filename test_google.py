import asyncio
from playwright.async_api import async_playwright


async def test_google():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Test 1: Page Load Validation
        print("Running Test 1: Page Load Validation...")
        await page.goto("https://www.google.com")
        assert "Google" in await page.title(), "Page load failed: Title does not contain 'Google'"
        print("✅ Test 1 Passed: Google homepage loaded successfully.")

        # Test 2: Search Functionality
        print("Running Test 2: Search Functionality...")
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("Playwright Python automation")
        await search_box.press("Enter")
        await page.wait_for_load_state("networkidle")
        assert "Playwright" in await page.title(), "Search test failed: Results page did not load"
        print("✅ Test 2 Passed: Search results loaded successfully.")

        # Test 3: Screenshot Capture
        print("Running Test 3: Screenshot Capture...")
        await page.screenshot(path="screenshot.png")
        print("✅ Test 3 Passed: Screenshot saved as 'screenshot.png'.")

        await browser.close()
        print("\n✅ All tests passed successfully.")


if __name__ == "__main__":
    asyncio.run(test_google())
