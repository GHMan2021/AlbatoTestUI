import pytest
from playwright.sync_api import sync_playwright, ViewportSize


@pytest.fixture(scope="session")
def playwright_sync():
    with sync_playwright() as p:
        yield p


@pytest.fixture(params=["chromium"])  # "webkit", "firefox"
def browser(request, playwright_sync):
    browser_type = request.param
    if browser_type == "chromium":
        browser_instance = playwright_sync.chromium.launch(headless=True)
    elif browser_type == "webkit":
        browser_instance = playwright_sync.webkit.launch(headless=True)
    elif browser_type == "firefox":
        browser_instance = playwright_sync.webkit.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    viewport: ViewportSize = {"width": 1920, "height": 1080}
    context = browser_instance.new_context(viewport=viewport)
    context.set_default_timeout(30000)
    page = context.new_page()

    yield page

    context.close()
    browser_instance.close()
