import time

from selenium.common import ElementClickInterceptedException, StaleElementReferenceException

from pages.main_page import BannerClose
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage



class TestSmokeOneProduct:

    def test_buy_product(self, driver):
        product = ProductPage(driver, 'https://www.mosoboi.ru/catalog/morris-co-arhive/112876/')
        product.open()
        try:
            product.increase_the_number()
        except ElementClickInterceptedException:
            close = BannerClose(driver, 'https://www.mosoboi.ru/personal/cart/')
            close.close_banner()
            product.increase_the_number()
        title_product = product.add_to_cart()
        product.go_to_cart()
        cart = CartPage(driver, 'https://www.mosoboi.ru/personal/cart/')
        title_product_cart = cart.checking_the_cart()
        assert title_product in title_product_cart, 'Названия коллекций не совпадают'
        cart.click_button_place_order()
        order = OrderPage(driver, 'https://www.mosoboi.ru/personal/order/make/')
        order.filling_in_the_data()
        try:
            order.choosing_a_delivery_method()
            order.choosing_payment()
            # order.help_sealer()
        except StaleElementReferenceException:
            print("Не удалось(( Идём дальше!")
        # order.click_oform()



