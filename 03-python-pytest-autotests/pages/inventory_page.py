import allure
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    @allure.step("Добавить в корзину: {product_id}")
    def add_to_cart(self, product_id: str):
        self.page.locator(f"[data-test='add-to-cart-{product_id}']").click()

    @allure.step("Удалить из корзины: {product_id}")
    def remove_from_cart(self, product_id: str):
        self.page.locator(f"[data-test='remove-{product_id}']").click()
