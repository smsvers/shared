import pytest
import math
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time

@pytest.mark.need_review
@pytest.mark.need_review_1 # Иногда не успевает пройти
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/google-hacking_197/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.should_be_product_title_in_cart()
    page.should_be_product_price_in_cart()
    time.sleep(5)

@pytest.mark.need_review_custom_scenarios
@pytest.mark.need_review_1 # Иногда не успевает пройти
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.should_not_be_message_on_product_added_to_cart()


@pytest.mark.xfail(reason="message remains after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.should_not_be_message_on_product_added_to_cart()

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/we-are-anonymous_192/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/we-are-anonymous_192/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser,link)
    page.should_be_login_url()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/we-are-anonymous_192/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_no_products_in_cart()
    page.should_be_empty_cart_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        mail = str('asd', time()) + "@mail.ru"
        pw = str('asd', time())
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        login_page.open()
        login_page.register_new_user(mail, pw)
        current_url = str(browser.current_url)
        login_page_with_user = LoginPage(browser, current_url)
        login_page_with_user.check_if_logged_in()
        login_page_with_user.should_not_be_login_url()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link) 
        page.add_to_cart()
        page.should_be_product_title_in_cart()
        page.should_be_product_price_in_cart()
        time.sleep(5)

    @pytest.mark.need_review_custom_scenarios
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  
        page.open()
        page.should_not_be_message_on_product_added_to_cart()
