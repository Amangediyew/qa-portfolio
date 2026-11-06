import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, "rep_" + call.when, outcome.get_result())


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def logged_in(login_page):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
