import allure
from playwright.sync_api import Page, expect, Locator

from components.base_component import BaseComponent


class ItemCardComponent(BaseComponent):
    def __init__(self, page: Page, root: Locator):
        super().__init__(page)
        self.root = root

        self.name = root.locator('[data-test="inventory-item-name"]')
        self.price = root.locator('[data-test="inventory-item-price"]')
        self.add_to_cart_btn = root.get_by_role("button", name="Add to cart")
        self.remove_btn = root.get_by_role("button", name="Remove")

    def get_price(self) -> float:
        text = self.price.inner_text()
        return float(text.replace("$", ""))

    @allure.step("Нажать на кнопку={button}")
    def click_on_btn(self, button):
        expect(button).to_be_visible()
        button.click()
