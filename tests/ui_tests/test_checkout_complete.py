import allure
import pytest
from faker import Faker

faker = Faker()


@allure.epic("Swag Labs")
class TestCheckoutCompletePage:

    @pytest.mark.smoke
    @allure.story("Оформление заказа с добавлением товара в корзину и оплатой")
    def test_user_can_complete_purchase(
        self,
        create_cart,
        cart_page,
        checkout_step_one_page,
        checkout_step_two_page,
        checkout_complete,
    ):
        cart_page.click_checkout_btn()
        checkout_step_one_page.enter_first_name(faker.first_name())
        checkout_step_one_page.enter_last_name(faker.last_name())
        checkout_step_one_page.enter_postal_code(faker.postalcode())
        checkout_step_one_page.click_continue_btn()

        with allure.step(
            f"Провека, перечень товаров в заказе верный={checkout_step_two_page.get_items_cart()}"
        ):
            assert set(create_cart) == set(
                checkout_step_two_page.get_items_cart()
            ), "Корзина с товарами не совпадает"

        with allure.step("Провека, сумма заказа верная"):
            assert (
                checkout_step_two_page.get_total_cost_cart()
                == checkout_step_two_page.get_subtotal()
            ), "Сумма заказа неверна"

        checkout_step_two_page.click_finish_btn()

        with allure.step("Провека, сообщение о успешном завершении заказа"):
            assert (
                checkout_complete.get_complete_purchase_msg() == "Checkout: Complete!"
            ), "Заказ не завершен"

    @pytest.mark.smoke
    @allure.story("Оформление заказа с пустой корзиной товаров")
    def test_user_purchase_with_empty_cart(
        self,
        auth,
        inventory_page,
        cart_page,
        checkout_step_one_page,
        checkout_step_two_page,
        checkout_complete,
    ):
        inventory_page.open_cart()
        cart_page.click_checkout_btn()
        checkout_step_one_page.enter_first_name(faker.first_name())
        checkout_step_one_page.enter_last_name(faker.last_name())
        checkout_step_one_page.enter_postal_code(faker.postalcode())
        checkout_step_one_page.click_continue_btn()
        checkout_step_two_page.click_finish_btn()

        with allure.step("Провека, сообщение о успешном завершении заказа"):
            assert (
                checkout_complete.get_complete_purchase_msg() == "Checkout: Complete!"
            ), "Заказ не завершен"
