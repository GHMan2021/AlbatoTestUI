import random

import allure
from playwright.sync_api import Page

from components.item_card_component import ItemCardComponent
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_sort_container = page.locator(
            '[data-test="product-sort-container"]'
        )
        self.all_item_prices = page.locator('[data-test="inventory-item-price"]')
        self.all_buttons_add_to_cart = page.get_by_role("button", name="Add to cart")
        self.cart_link_button = page.locator('[data-test="shopping-cart-link"]')
        self.card_locators = page.locator('[data-test="inventory-item"]')

    @property
    def item_cards(self) -> list[ItemCardComponent]:
        return [ItemCardComponent(self.page, card) for card in self.card_locators.all()]

    @allure.step("Выбрать сортировку вида={item_name}")
    def select_item_by_name(self, item_name) -> None:
        self.wait_for_element(self.product_sort_container)
        self.product_sort_container.select_option(label=item_name)

    def get_all_prices(self) -> list[float]:
        list_elements = self.all_item_prices.all()
        list_prices = []
        for i in list_elements:
            val = i.inner_text().replace("$", "")
            list_prices.append(float(val))
        return list_prices

    def get_sort_all_price_by_asc(self) -> list[float]:
        list_prices = self.get_all_prices()
        list_prices.sort()
        return list_prices

    @allure.step("Добавить случайный набор товаров в корзину")
    def get_random_cart(self) -> list[tuple[str, float]]:
        count = random.randint(1, len(self.item_cards))
        selected_cards = random.sample(self.item_cards, count)
        list_card_info = []
        for card in selected_cards:
            name = card.name.inner_text()
            price = card.get_price()
            list_card_info.append((name, price))
            card.add_to_cart_btn.click()

        with allure.step(f"Список товаров={list_card_info}"):
            return list_card_info

    @allure.step("Открыть заказ")
    def open_cart(self) -> None:
        self.wait_for_element(self.cart_link_button)
        self.cart_link_button.click()
