import os

import pytest
from dotenv import load_dotenv

from pages.cart_page import CartPage
from pages.ckeckout_complete import CheckoutCompletePage
from pages.ckeckout_step_one_page import CheckoutStepOnePage
from pages.ckeckout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

load_dotenv()


@pytest.fixture()
def auth(browser):
    login_page = LoginPage(browser)
    login_page.auth(login=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))


@pytest.fixture()
def inventory_page(browser):
    return InventoryPage(browser)


@pytest.fixture()
def cart_page(browser):
    return CartPage(browser)


@pytest.fixture()
def checkout_step_one_page(browser):
    return CheckoutStepOnePage(browser)


@pytest.fixture()
def checkout_step_two_page(browser):
    return CheckoutStepTwoPage(browser)


@pytest.fixture()
def checkout_complete(browser):
    return CheckoutCompletePage(browser)


@pytest.fixture()
def create_cart(auth, inventory_page, cart_page):
    list_item_info = inventory_page.get_random_cart()  # [(name, price),..]
    inventory_page.open_cart()
    yield list_item_info
    cart_page.clear_cart()
