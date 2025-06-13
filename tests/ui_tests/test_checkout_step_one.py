from playwright.sync_api import expect
from faker import Faker

faker = Faker()


class TestCheckoutStepOnePage:

    def test_checkout_wo_authorization(
        self, create_cart, cart_page, checkout_step_one_page
    ):
        cart_page.click_checkout_btn()
        checkout_step_one_page.click_continue_btn()

        expect(checkout_step_one_page.error_msg, "Алерт не виден").to_be_visible()
        expect(checkout_step_one_page.error_msg, "Текст алерта неверный").to_have_text(
            "Error: First Name is required"
        )

    def test_checkout_wo_postal_code(
        self, create_cart, cart_page, checkout_step_one_page
    ):
        cart_page.click_checkout_btn()
        checkout_step_one_page.enter_first_name(faker.first_name())
        checkout_step_one_page.enter_last_name(faker.last_name())
        checkout_step_one_page.click_continue_btn()

        expect(checkout_step_one_page.error_msg, "Алерт не виден").to_be_visible()
        expect(checkout_step_one_page.error_msg, "Текст алерта неверный").to_have_text(
            "Error: Postal Code is required"
        )
