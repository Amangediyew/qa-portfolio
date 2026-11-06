import allure
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.submit = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    @allure.step("Открыть страницу логина")
    def open(self):
        self.page.goto("/")

    @allure.step("Войти как {user}")
    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        self.submit.click()
