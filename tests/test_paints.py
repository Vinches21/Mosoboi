import time

from pages.paint_page import PaintPage



class TestPaintsFilter:

    """Проверка назаначения краски"""
    def test_checking_the_destination(self, driver):
        destination = PaintPage(driver, 'https://www.mosoboi.ru/kraski/')
        destination.open()
        destination.comparison_of_destination_properties()



    def test_cheking_gloss(self, driver):
        gloss = PaintPage(driver, 'https://www.mosoboi.ru/kraski/')
        gloss.open()
        gloss.choose_a_gloss()

    def test_checking_basis(self, driver):
        basis = PaintPage(driver, 'https://www.mosoboi.ru/kraski/')
        basis.open()
        basis.choosing_the_basis()
        time.sleep(5)


    def test_whatssapp_click(self, driver):
        whats = PaintPage(driver, 'https://www.mosoboi.ru/kraski/')
        whats.open()
        whats.click_icon_whatsapp()