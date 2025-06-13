import allure

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.continue_btn = page.locator('[data-test="continue"]')
        self.error_msg = page.locator('[data-test="error"]')
        self.first_name_field = page.locator('[data-test="firstName"]')
        self.last_name_field = page.locator('[data-test="lastName"]')
        self.postal_code_field = page.locator('[data-test="postalCode"]')

    def click_continue_btn(self) -> None:
        self.wait_for_element(self.continue_btn)
        self.continue_btn.click()

    def enter_first_name(self, first_name) -> None:
        self.wait_for_element(self.first_name_field)
        self.first_name_field.fill(first_name)

    def enter_last_name(self, last_name) -> None:
        self.wait_for_element(self.last_name_field)
        self.last_name_field.fill(last_name)

    def enter_postal_code(self, postal_code) -> None:
        self.wait_for_element(self.postal_code_field)
        self.postal_code_field.fill(postal_code)
