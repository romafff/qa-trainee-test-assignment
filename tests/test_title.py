import pytest
from playwright.sync_api import sync_playwright

URL = "https://playwright.dev/"
EXPECTED_HEADING = "Playwright enables reliable end-to-end testing for modern web apps."


@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_main_heading(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        heading = page.locator("h1").inner_text().strip()
        assert heading == EXPECTED_HEADING
        browser.close()