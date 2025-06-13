import allure

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.remove_btn = page.get_by_role("button", name="Remove")

    def click_checkout_btn(self) -> None:
        self.wait_for_element(self.checkout_btn)
        self.checkout_btn.click()

    def clear_cart(self) -> None:
        list_remove = self.remove_btn.all()
        for i in list_remove:
            i.click()
