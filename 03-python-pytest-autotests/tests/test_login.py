import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешный вход")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, page, login_page):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    @allure.title("Ошибка при неверных данных: {user}")
    @pytest.mark.parametrize("user,password,message", [
        ("standard_user", "wrong", "Username and password do not match"),
        ("locked_out_user", "secret_sauce", "this user has been locked out"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ])
    def test_invalid_login(self, login_page, user, password, message):
        login_page.open()
        login_page.login(user, password)
        expect(login_page.error).to_contain_text(message)
