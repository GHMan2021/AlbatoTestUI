import allure
from playwright.sync_api import Page, expect, Response


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_element(self, locator, timeout=25000):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        expect(locator).to_be_attached(timeout=timeout)
        expect(locator).to_be_visible(timeout=timeout)
        expect(locator).to_be_enabled(timeout=timeout)
