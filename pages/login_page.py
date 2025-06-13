import allure

from pages.base_page import BasePage
from config.links import BASE_URL


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.input_login = page.locator('[data-test="username"]')
        self.input_password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def auth(self, login, password):
        self.open(BASE_URL)
        self.wait_for_element(self.input_login)
        with allure.step(f"Авторизоваться с логином={login} и паролем={password}"):
            self.input_login.fill(login)
            self.wait_for_element(self.input_password)
            self.input_password.fill(password)
            self.login_button.click()
