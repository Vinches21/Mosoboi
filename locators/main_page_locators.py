from selenium.webdriver.common.by import By

class MainPageLocators:

    BANNER_CLOSE = (By.CSS_SELECTOR, "#weekendOrderForm > div.close")




class SearchLocators:

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='title-search-input']")
    SEARCH_CLICK = (By.CSS_SELECTOR, "#search_mobile > input.img")
    ARTICLE_OUTPUT = (By.CSS_SELECTOR, "a[class='kollect-name']")

class FooterLocators:

    FORM_COMPLAINT = (By.CSS_SELECTOR, "a[class='compliant-form']")
    CAPTCHA = (By.CSS_SELECTOR, "#cboxLoadedContent > div > form > label.field_captcha_wrap > span > img")