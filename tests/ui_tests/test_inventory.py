import allure
import pytest


@allure.epic("Swag Labs")
class TestInventoryPage:

    @pytest.mark.smoke
    @allure.story("Сортировка товаров по возрастанию цены")
    def test_sort_inventory_items(self, auth, inventory_page):
        inventory_page.select_item_by_name("Price (low to high)")

        get_all_prices = inventory_page.get_all_prices()
        get_all_prices_sorted = inventory_page.get_sort_all_price_by_asc()
        with allure.step(
            f"Провека, что товары отсортированы по цене={get_all_prices_sorted}"
        ):
            assert (
                get_all_prices_sorted == get_all_prices
            ), "Товары не отсортированы по возрастанию цены"
