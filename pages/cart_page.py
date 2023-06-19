import time

from pages.base_page import BasePage
from locators.cart_locators import CartLocators



class CartPage(BasePage):
    locators = CartLocators()

    def checking_the_cart(self):
        title_product_cart = self.elements_is_present(self.locators.TITLE_FACTORY).text.split('\n')[2].replace('Коллекция ', '')
        return title_product_cart
        time.sleep(5)

    def click_button_place_order(self):
        self.elements_is_clickable(self.locators.BUTON_PLACE_ORDER).click()


    def increase_the_number(self):
        self.elements_is_clickable(self.locators.BUTTON_INCREASE).click()

    def reduce_the_number(self):
        self.elements_is_clickable(self.locators.BUTTON_REDUCE).click()

    def delete_product(self):
        self.elements_is_clickable(self.locators.DELETE_PRODUCT).click()
        assert self.elements_is_present(self.locators.CART_EMPTY).text == 'Ваша корзина пуста', 'Корзина не пуста'