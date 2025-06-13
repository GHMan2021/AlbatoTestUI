import allure

from components.item_card_cart_component import ItemCardCartComponent
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.finish_btn = page.locator('[data-test="finish"]')
        self.card_locators = page.locator('[data-test="inventory-item"]')
        self.subtotal = page.locator('[data-test="subtotal-label"]')

    @property
    def item_cards_cart(self) -> list[ItemCardCartComponent]:
        return [
            ItemCardCartComponent(self.page, card) for card in self.card_locators.all()
        ]

    @allure.step("Клик кнопки 'Finish'")
    def click_finish_btn(self) -> None:
        self.wait_for_element(self.finish_btn)
        self.finish_btn.click()

    def get_items_cart(self) -> list[tuple[str, float]]:
        list_card_info = []
        for card in self.item_cards_cart:
            name = card.name.inner_text()
            price = card.get_price()
            list_card_info.append((name, price))

        return list_card_info

    def get_subtotal(self) -> str:
        self.wait_for_element(self.subtotal)
        inner_text = self.subtotal.inner_text()
        subtotal = inner_text.replace("Item total: $", "")
        return subtotal

    def get_total_cost_cart(self) -> str:
        list_cart_info = self.get_items_cart()
        total_cost = 0
        for _, price in list_cart_info:
            total_cost += price
        return str(total_cost)
