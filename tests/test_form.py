import random
import time


from pages.form_page import FormComplaint, FormSearchImage, FormSelectionByParameters, FormOrderOneClick, \
FormSelectionPaintBanner, FormSpecialPrice, FormFoundCheaper, FormCalculator


class TestForm:
    """Проверка заполнения формы Рекламация"""
    def test_complaint_forms(self, driver):
        complaint_forms = FormComplaint(driver, 'https://www.mosoboi.ru/otdel-reklamacij/')
        complaint_forms.open()
        complaint_forms.filling_out_the_complaint()
        complaint_forms.get_screen()

    """Форма Обратный звонок"""
    def test_callback(self, driver):
        callback_form = FormComplaint(driver, 'https://www.mosoboi.ru/vozvrat-obmen/')
        callback_form.open()
        callback_form.callback()

    """Заполнение формы Поиск по Изображению"""

    def test_search_image(self, driver):
        search_image = FormSearchImage(driver, 'https://www.mosoboi.ru/podbor-po-izobrazheniyu/')
        search_image.open()
        search_image.filling_out_the_image_search()


    """Заполнение формы подбор по параметрам"""
    def test_selection_by_parameters(self, driver):
        selection_by_parameters = FormSelectionByParameters(driver, 'https://www.mosoboi.ru/catalog/a-grifoni/')
        selection_by_parameters.open()
        selection_by_parameters.filling_selection_by_parameters_form()


    """Заполнения формы Заказ в 1 клик"""
    def test_order_one_click(self, driver):
        order_one_click = FormOrderOneClick(driver, 'https://www.mosoboi.ru/catalog/legacy/')
        order_one_click.open()
        order_one_click.checking_the_amount()
        order_one_click.completion_order_one_click()


    def test_selection_paint_banner(self, driver):
        selection_paint = FormSelectionPaintBanner(driver, 'https://www.mosoboi.ru/kraski/')
        selection_paint.open()
        selection_paint.filling_form_selection_paint()

    """Заполнение формы Уточнение специальной цены"""
    def test_clarification_of_the_special_price(self, driver):
        special_price = FormSpecialPrice(driver, 'https://www.mosoboi.ru/catalog/morris-co-arhive/')
        special_price.open()
        special_price.filling_special_price()

    """Заполнение формы Нашли дешевле"""
    def test_found_cheaper(self, driver):
        found_cheaper = FormFoundCheaper(driver, 'https://www.mosoboi.ru/catalog/morris-co-arhive/112876/')
        found_cheaper.open()
        found_cheaper.filling_found_cheaper()

class TestCalculator:
    """Расчет количество рулонов на калькуляторе"""
    def test_counting_the_quantity_on_the_calculator(self, driver):
        counting_quantity = FormCalculator(driver, 'https://www.mosoboi.ru/catalog/morris-co-arhive/112876/')
        counting_quantity.open()
        counting_quantity.filling_calculator()
