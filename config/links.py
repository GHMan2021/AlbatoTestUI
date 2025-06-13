from enum import Enum


class Link(str, Enum):

    URL = "https://www.saucedemo.com"
    INVENTORY = f"{URL}/inventory.html"
    CART = f"{URL}/cart.html"
    CHECKOUT_STEP_1 = f"{URL}/checkout-step-one.html"
    CHECKOUT_STEP_2 = f"{URL}/checkout-step-two.html"
    CHECKOUT_COMPLETE = f"{URL}/checkout-complete.html"
