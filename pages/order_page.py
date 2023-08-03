import random
import time

from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    locators = OrderLocators()

    def filling_in_the_data(self):
        self.elements_is_visible(self.locators.NAME).send_keys('Ivanov Test')
        self.elements_is_visible(self.locators.EMAIL).send_keys(f'test{random.randint(1, 100)}@mail.ru')
        time.sleep(2)
        self.elements_is_visible(self.locators.PHONE).send_keys('79001000000')
        self.elements_is_visible(self.locators.CITY).clear()
        self.elements_is_visible(self.locators.CITY).send_keys('Moscow')
        # self.elements_is_visible(self.locators.ADDRESS).send_keys('Каретный переулок, 20')
        self.elements_is_visible(self.locators.COMMENT).send_keys('Тестовый текст')



    def choosing_a_delivery_method(self):
        cdek = self.locators.CDEK
        leninskiy_24 = self.locators.LENINSKIY_24
        voykovskaya = self.locators.VOYKOVSKAYA
        govorovo = self.locators.GOVOROVO
        avtozavodskaya = self.locators.AVTOZAVODSKAYA
        terminal_transport = self.locators.TERMINAL_TRANSPORT
        flat_transport = self.locators.FLAT_TRANSPORT
        delivery = [cdek, leninskiy_24, voykovskaya, govorovo,
                    avtozavodskaya, terminal_transport, flat_transport]

        self.elements_is_clickable(random.choice(delivery)).click()


    def choosing_payment(self):
        sberbank = self.locators.SBERBANK
        online_payment = self.locators.ONLINE_PAYMENT
        credit = self.locators.CREDIT
        bank_transfer = self.locators.BANK_TRANSFER
        payment = [sberbank, online_payment, credit, bank_transfer]

        self.elements_is_clickable(random.choice(payment)).click()

    def help_sealer(self):
        self.elements_is_clickable(self.locators.BUTTON_SEALER).click()
        self.elements_is_clickable(self.locators.BUTTON_SELECT).click()
        showroom = ['LENINSKIY', 'ROOMER', 'FIMILYROOM', 'GOVOROVO']
        x = self.elements_is_visible(self.locators.BUTTON_SELECT)
        drop = Select(x)
        drop.select_by_value(random.choice(showroom))
        time.sleep((2))
        # self.elements_is_clickable((By.CSS_SELECTOR, f'select[id="ORDER_PROP_30"] option[value="{random.choice(showroom)}"]')).click()

    def click_oform(self):
        self.elements_is_clickable(self.locators.BUTTON_ORDER).click()