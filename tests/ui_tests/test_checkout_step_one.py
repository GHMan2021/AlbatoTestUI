import allure
import pytest
from faker import Faker
from playwright.sync_api import expect

faker = Faker()


@allure.epic("Swag Labs")
class TestCheckoutStepOnePage:

    @pytest.mark.smoke
    @allure.story("Переход к оформлению заказа без авторизации")
    def test_checkout_wo_authorization(
        self, create_cart, cart_page, checkout_step_one_page
    ):
        cart_page.click_checkout_btn()
        checkout_step_one_page.click_continue_btn()

        with allure.step(
            "Провека, показано сообщение об ошибки 'Error: First Name is required'"
        ):
            expect(checkout_step_one_page.error_msg, "Алерт не виден").to_be_visible()
            expect(
                checkout_step_one_page.error_msg, "Текст алерта неверный"
            ).to_have_text("Error: First Name is required")

    @pytest.mark.smoke
    @allure.story("Оформление заказа с пустым полем 'Zip/Postal Code'")
    def test_checkout_wo_postal_code(
        self, create_cart, cart_page, checkout_step_one_page
    ):
        cart_page.click_checkout_btn()
        checkout_step_one_page.enter_first_name(faker.first_name())
        checkout_step_one_page.enter_last_name(faker.last_name())
        checkout_step_one_page.click_continue_btn()

        with allure.step(
            "Провека, показано сообщение об ошибки 'Error: Postal Code is required'"
        ):
            expect(checkout_step_one_page.error_msg, "Алерт не виден").to_be_visible()
            expect(
                checkout_step_one_page.error_msg, "Текст алерта неверный"
            ).to_have_text("Error: Postal Code is required")
