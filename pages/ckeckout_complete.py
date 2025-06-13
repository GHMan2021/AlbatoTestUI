from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.checkout_complete_text = page.locator('[data-test="title"]')

    def get_complete_purchase_msg(self) -> str:
        self.wait_for_element(self.checkout_complete_text)
        return self.checkout_complete_text.inner_text()
