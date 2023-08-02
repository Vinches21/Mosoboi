from  selenium.webdriver.common.by import By

class ProductLocators:
    TITTLE_PRODUCT = (By.CSS_SELECTOR, 'h1[id="h1-pages"]')

    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'div.third-line a.add2basket')
    BUTTON_INCREASE = (By.CSS_SELECTOR, 'div.third-line div.plus.basket_kolvo-btn')
    BUTTON_REDUCE = (By.CSS_SELECTOR, 'div.third-line div.minus.basket_kolvo-btn')

    BUTTON_GO_TO_CART = (By.CSS_SELECTOR, 'div.btn_to_basket > a')
    BUTTON_MAKE_ORDER = (By.CSS_SELECTOR, 'div.btn_to_order > a')