import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class ItemCardCartComponent(BaseComponent):
    def __init__(self, page: Page, root: Locator):
        super().__init__(page)
        self.root = root

        self.name = root.locator('[data-test="inventory-item-name"]')
        self.price = root.locator('[data-test="inventory-item-price"]')

    @allure.step("Получить цену товара")
    def get_price(self) -> float:
        text = self.price.inner_text()
        return float(text.replace("$", ""))
