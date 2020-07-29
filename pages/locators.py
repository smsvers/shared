from selenium.webdriver.common.by import By
# Каждый класс будет соответствовать каждому классу PageObject
# селектор — это пара: как искать и что искать.

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PAGE_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_ADDED_TITLE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner')


class BasketPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    CART_PRODUCT_SUM = (By.CSS_SELECTOR, ".col-sm-1 .price_color.align-right")
    EMPTY_CART_MESSAGE = (By.ID, "content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')
    REGISTER_SUCCESS_BOX = (By.CSS_SELECTOR,".icon-ok-sign")
    LOG_OUT_BUTTON = (By.ID, 'logout_link')

