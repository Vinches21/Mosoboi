import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import SearchLocators, FooterLocators




class Search(BasePage):

    locators = SearchLocators()

    def search_input(self, article):
        self.elements_is_visible(self.locators.SEARCH_INPUT).send_keys(article)
        self.elements_is_visible(self.locators.SEARCH_CLICK).click()
        output_article = self.elements_is_present(self.locators.ARTICLE_OUTPUT).text.split()[-1]
        return output_article


class Footer(BasePage):

    locators = FooterLocators()

    def footer_captcha(self):
        button_captcha = self.elements_is_visible(self.locators.FORM_COMPLAINT)
        self.go_to_element(button_captcha)
        button_captcha.click()
        captcha = self.elements_is_present(self.locators.CAPTCHA).get_attribute('src')
        print(captcha)


class Main_page:
    pass