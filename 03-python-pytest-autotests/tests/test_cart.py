import allure
from playwright.sync_api import expect

BACKPACK = "sauce-labs-backpack"
LIGHT = "sauce-labs-bike-light"


@allure.feature("Корзина")
@allure.severity(allure.severity_level.NORMAL)
class TestCart:

    @allure.title("Добавление товара увеличивает счётчик корзины")
    def test_add_item(self, logged_in, inventory_page):
        inventory_page.add_to_cart(BACKPACK)
        expect(inventory_page.cart_badge).to_have_text("1")

    @allure.title("Добавление двух товаров")
    def test_add_two_items(self, logged_in, inventory_page):
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.add_to_cart(LIGHT)
        expect(inventory_page.cart_badge).to_have_text("2")

    @allure.title("Удаление товара убирает счётчик")
    def test_remove_item(self, logged_in, inventory_page):
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.remove_from_cart(BACKPACK)
        expect(inventory_page.cart_badge).to_have_count(0)

    @allure.title("Товар отображается на странице корзины")
    def test_item_in_cart_page(self, logged_in, inventory_page, page):
        inventory_page.add_to_cart(BACKPACK)
        inventory_page.cart_link.click()
        expect(page.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")
