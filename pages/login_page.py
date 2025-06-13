import allure

from pages.base_page import BasePage
from config.links import Link


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.input_login = page.locator('[data-test="username"]')
        self.input_password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    @allure.step("Авторизоваться с логином={login} и паролем={password}")
    def auth(self, login, password):
        self.open(Link.URL)
        self.wait_for_element(self.input_login)
        self.input_login.fill(login)
        self.wait_for_element(self.input_password)
        self.input_password.fill(password)
        self.login_button.click()
