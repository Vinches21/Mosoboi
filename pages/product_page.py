import time


from pages.base_page import BasePage

from locators.product_locators import ProductLocators


class ProductPage(BasePage):
    locators = ProductLocators()

    """Перейти в корзину"""
    def add_to_cart(self):
        title_product = self.elements_is_present(self.locators.TITTLE_PRODUCT).text.split()[-2]
        self.elements_is_clickable(self.locators.BUTTON_ADD_TO_CART).click()
        return title_product

    """Перейти на страницу оформления заказа, заполнения персональных данных"""
    def make_the_order(self):
        self.elements_is_clickable(self.locators.BUTTON_MAKE_ORDER).click()


    def go_to_cart(self):
        self.elements_is_clickable(self.locators.BUTTON_GO_TO_CART).click()


    """Увеличить количество товара"""
    def increase_the_number(self):
        for _ in range(5):
            self.elements_is_clickable(self.locators.BUTTON_INCREASE).click()

    """Уменьшить количество товара"""

    def reduce_the_number(self):
        self.elements_is_clickable(self.locators.BUTTON_REDUCE).click()