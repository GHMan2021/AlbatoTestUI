class TestInventoryPage:

    def test_sort_inventory_items(self, auth, inventory_page):
        inventory_page.select_item_by_name("Price (low to high)")

        get_all_prices = inventory_page._get_all_prices()
        get_all_prices_sorted = inventory_page._sort_all_price_by_asc()
        assert (
            get_all_prices_sorted == get_all_prices
        ), "Товары не отсортированы по возрастанию цены"
