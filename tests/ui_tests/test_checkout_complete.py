from faker import Faker

faker = Faker()


class TestCheckoutCompletePage:

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

        assert set(create_cart) == set(
            checkout_step_two_page._get_items_cart()
        ), "Корзина с товарами не совпадает"

        assert (
            checkout_step_two_page._get_total_cost_cart()
            == checkout_step_two_page._get_subtotal()
        ), "Сумма заказа неверна"

        checkout_step_two_page.click_finish_btn()

        assert (
            checkout_complete._get_complete_purchase_msg() == "Checkout: Complete!"
        ), "Заказ не завершен"

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

        assert (
            checkout_complete._get_complete_purchase_msg() == "Checkout: Complete!"
        ), "Заказ не завершен"
