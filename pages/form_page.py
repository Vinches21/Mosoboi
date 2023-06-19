import os
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

from generator.generator import generated_person, generated_file_jpg

from locators.form_locators import ComplaintFormLocators, CallbacklLocators, SearchImageLocators, SelectionByParametersLocators,\
    FormOrderOneClickLocators, FormSelectionPaintBannerLocators, FormSpecialPriceLocators, FormFoundCheaperLocators, \
    FormCalculatorLocators

class FormComplaint(BasePage):

    locators = ComplaintFormLocators()
    locators_call = CallbacklLocators()

    def filling_out_the_complaint(self):
        form = next(generated_person())
        fio = form.fio
        address = form.address
        phone = form.phone
        email = form.email
        order_number = form.order_number
        order_date = form.order_date
        brand = form.brand
        collection = form.collection
        article = form.article
        part_number = form.part_number
        quantity = form.quantity
        deffect_quantity = form.deffect_quantity
        opened_quantity = form.opened_quantity
        closed_quantity = form.closed_quantity
        used_quantity = form.used_quantity
        message = form.message
        self.go_to_element(self.elements_is_visible(self.locators.FIO))
        self.elements_is_visible(self.locators.FIO).send_keys(fio)
        self.elements_is_visible(self.locators.ADDRESS).send_keys(address)
        self.elements_is_visible(self.locators.PHONE).send_keys(phone)
        self.elements_is_visible(self.locators.EMAIL).send_keys(email)
        self.elements_is_visible(self.locators.ORDER_NUMBER).send_keys(order_number)
        self.elements_is_visible(self.locators.ORDER_DATE).send_keys(order_date)
        self.elements_is_visible(self.locators.BRAND).send_keys(brand)
        self.elements_is_visible(self.locators.COLLECTION).send_keys(collection)
        self.elements_is_visible(self.locators.ARTICLE).send_keys(article)
        self.elements_is_visible(self.locators.PART_NUMBER).send_keys(part_number)
        self.elements_is_visible(self.locators.QUANTITY).send_keys(quantity)
        self.elements_is_visible(self.locators.DEFECT_QUANTITY).send_keys(deffect_quantity)
        self.elements_is_visible(self.locators.OPENED_QUANTITY).send_keys(opened_quantity)
        self.elements_is_visible(self.locators.CLOSED_QUANTITY).send_keys(closed_quantity)
        self.elements_is_visible(self.locators.USED_QUANTITY).send_keys(used_quantity)
        self.elements_is_visible(self.locators.MESSAGE).send_keys(message)
        self.elements_is_visible(self.locators.RADIO_DEFECT).click()
        self.elements_is_visible(self.locators.RADIO_REQUIREMENT).click()
        num = 1
        for i in range(3):
            file_name, path = generated_file_jpg()
            self.elements_is_present((By.CSS_SELECTOR, f'input[type="file"][name="photo-{num}"]')).send_keys(path)
            time.sleep(1)
            os.remove(path)
            num+=1

    def callback(self):
        self.elements_is_visible(self.locators_call.BUTTON_CALL).click()
        self.elements_is_visible(self.locators_call.NAME).send_keys('Иванов Иван')
        self.elements_is_visible(self.locators_call.NUMBER).send_keys('9002001010')
        self.elements_is_visible(self.locators_call.BUTTON_SEND).click()


class FormSearchImage(BasePage):
    locators = SearchImageLocators()


    def filling_out_the_image_search(self):
        form = next(generated_person())
        name = form.fio
        phone = form.phone
        email = form.email
        city = form.city
        message = form.message
        self.go_to_element(self.elements_is_visible(self.locators.NAME))
        self.elements_is_visible(self.locators.NAME).send_keys(name)
        self.elements_is_visible(self.locators.PHONE).send_keys(phone)
        self.elements_is_visible(self.locators.EMAIL).send_keys(email)
        self.elements_is_visible(self.locators.CITY).send_keys(city)
        self.elements_is_visible(self.locators.MESSAGE).send_keys(message)
        file_name, path = generated_file_jpg()
        self.elements_is_present(self.locators.BUTTON_ADD_FILE).send_keys(path)
        output = self.elements_is_present(self.locators.TEXT_FILE).text
        assert file_name.split('\\')[-1] == output, 'The files are diffrent'
        os.remove(path)
        # self.elements_is_visible(self.locators.BUTTON_SEND).click()

class FormSelectionByParameters(BasePage):

    locators = SelectionByParametersLocators()

    def filling_selection_by_parameters_form(self):
        people = next(generated_person())
        name= people.fio
        phone = people.phone
        email = people.email
        # self.go_to_element(self.elements_is_visible(self.locators.BUTTON_SEND_1))
        self.elements_is_clickable(self.locators.BUTTON_SEND_1).click()
        self.elements_is_visible(self.locators.NAME).send_keys(name)
        self.elements_is_visible(self.locators.PHONE).send_keys(phone)
        self.elements_is_visible(self.locators.EMAIL).send_keys(email)
        # self.elements_is_clickable(self.locators.BUTTON_SEND_2).click()

class FormOrderOneClick(BasePage):
    locators = FormOrderOneClickLocators()

    """Првоерка суммы"""
    def checking_the_amount(self):
        # element = self.driver.find_element(*self.locators.BUTTON_ONE_CLICK)
        element = self.driver.find_element(*self.locators.BUTTON_ONE_CLICK)
        self.click_hidden_element(element)
        price = self.elements_is_visible(self.locators.PRICE).text
        price_summ = int(price.replace(' ', '')) * 2
        self.elements_is_visible(self.locators.BUTTON_INCREASE).click()
        price_finish = self.elements_is_visible(self.locators.PRICE).text
        assert price_summ == int(price_finish.replace(' ', '')), 'The amount is not correct'


    def completion_order_one_click(self):
        self.elements_is_visible(self.locators.NAME).send_keys('Тестов Тест')
        self.elements_is_clickable(self.locators.PHONE).click()
        self.elements_is_visible(self.locators.PHONE).send_keys('9000000000')
        self.elements_is_visible(self.locators.EMAIL).send_keys('test@mail.ru')
        self.elements_is_visible(self.locators.MESSAGE).send_keys('Тестирование заказа в 1 клик')
        #self.elements_is_clickable(self.locators.BUTTON_SEND).click()


class FormSelectionPaintBanner(BasePage):
    locators = FormSelectionPaintBannerLocators()

    def filling_form_selection_paint(self):
        element = self.driver.find_element(*self.locators.BUNNER)
        self.click_hidden_element(element)
        self.elements_is_visible(self.locators.NAME).send_keys('Иванов Иван')
        self.elements_is_visible(self.locators.PHONE).send_keys('9000000000')
        self.elements_is_visible(self.locators.EMAIL).send_keys('test@mail.ru')
        # self.elements_is_visible(self.locators.BUTTON_SEND).click()

class FormSpecialPrice(BasePage):
    locators = FormSpecialPriceLocators()

    def filling_special_price(self):
        element = self.driver.find_element(*self.locators.BUTTON_SPECIAL_PRICE)
        self.click_hidden_element(element)
        self.elements_is_visible(self.locators.NAME).send_keys('Петров Тест')
        self.elements_is_visible(self.locators.PHONE).send_keys('9012223333')
        self.elements_is_visible(self.locators.EMAIL).send_keys('testtest@mail.ru')
        self.elements_is_visible(self.locators.MESSAGE).send_keys('Проверка формы Специальная цена')
        self.elements_is_visible(self.locators.CALLS_FROM).send_keys('10')
        self.elements_is_visible(self.locators.CALLS_TO).send_keys('18')
        self.elements_is_visible(self.locators.BUTTON_SEND).click()

class FormFoundCheaper(BasePage):
    locators = FormFoundCheaperLocators()

    def filling_found_cheaper(self):
        self.elements_is_clickable(self.locators.BUTTON_FOUND_CHEAPER).click()
        self.elements_is_visible(self.locators.NAME).send_keys('Тестовый Тест')
        self.elements_is_clickable(self.locators.PHONE).click()
        self.elements_is_visible(self.locators.PHONE).send_keys('9010010202')
        self.elements_is_visible(self.locators.EMAIL).send_keys('test1@mail.ru')
        self.elements_is_visible(self.locators.PRICE).send_keys('1200')
        self.elements_is_visible(self.locators.LINK).send_keys('https://oboi-ma.ru/')
        # self.elements_is_visible(self.locators.BUTTON_SEND).click()
        time.sleep(5)

class FormCalculator(BasePage):
    locators = FormCalculatorLocators()

    def filling_calculator(self):
        price_one = self.elements_is_present(self.locators.PRICE_ONE).text
        self.elements_is_clickable(self.locators.BUTTON_CALCULATOR).click()
        self.elements_is_visible(self.locators.HEIGHT).send_keys(str(round(random.uniform(2.2, 3.8), 2)))
        self.elements_is_visible(self.locators.WALL_1).send_keys(str(round(random.uniform(2, 7), 2)))
        self.elements_is_visible(self.locators.WALL_2).send_keys(str(round(random.uniform(2, 7), 2)))
        self.elements_is_visible(self.locators.WALL_3).send_keys(str(round(random.uniform(2, 7), 2)))
        self.elements_is_visible(self.locators.WALL_4).send_keys(str(round(random.uniform(2, 7), 2)))
        self.elements_is_visible(self.locators.DOOR).send_keys(str(round(random.uniform(0.5, 1.5), 2)))
        self.elements_is_visible(self.locators.WINDOW).send_keys(str(round(random.uniform(1, 2), 2)))
        self.elements_is_clickable(self.locators.BUTTON_RESULT).click()
        perimetr = self.elements_is_present(self.locators.PERIMETR_RESULT).text
        numbers_of_rolls = self.elements_is_present(self.locators.NUMBERS_OF_ROLLS).text
        summa = self.elements_is_present(self.locators.PRICE_SUMMA).text
        print((int(price_one.replace(' ', '')) * int(numbers_of_rolls)))
        print(int(summa.replace(' ', '')[:-4]))
        assert (int(price_one.replace(' ', '')) * int(numbers_of_rolls)) == int(summa.replace(' ', '')[:-4]), 'The amount does not match'

        time.sleep(5)