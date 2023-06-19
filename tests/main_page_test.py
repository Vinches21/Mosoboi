import random
import time

from pages.main_page import Search, Footer
from selenium.common.exceptions import TimeoutException





class TestSearch:

    def test_search_input(self, driver):
        search = Search(driver, 'https://www.mosoboi.ru/')
        search.open()
        search.close_banner()
        output_article = search.search_input('FF51504')
        assert 'FF51504' == output_article, 'The articles do not match'


class TestFooter:

    def test_complaint_form(self, driver):
        form = Footer(driver, 'https://www.mosoboi.ru/lepnina/')
        form.open()
        form.footer_captcha()
        # try:
        #     form.close_banner()
        # except TimeoutException:
        #     form.close_banner()