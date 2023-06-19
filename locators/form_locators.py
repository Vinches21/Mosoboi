from selenium.webdriver.common.by import By

class ComplaintFormLocators:

    #input items
    FIO = (By.CSS_SELECTOR, 'div.body input[name="name"]')
    ADDRESS = (By.CSS_SELECTOR, 'input[name="address"]')
    PHONE = (By.CSS_SELECTOR, 'div.body input[name="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'input[name="order-number"]')
    ORDER_DATE = (By.CSS_SELECTOR, 'input[name="order-date"]')
    BRAND = (By.CSS_SELECTOR, 'input[name="brand"]')
    COLLECTION = (By.CSS_SELECTOR, 'input[name="collection"]')
    ARTICLE = (By.CSS_SELECTOR, 'input[name="artnumber"]')
    PART_NUMBER = (By.CSS_SELECTOR, 'input[name="part-number"]')
    QUANTITY = (By.CSS_SELECTOR, 'input[name="quantity"]')
    DEFECT_QUANTITY = (By.CSS_SELECTOR, 'input[name="defect-quantity"]')
    OPENED_QUANTITY = (By.CSS_SELECTOR, 'input[name="opened-quantity"]')
    CLOSED_QUANTITY = (By.CSS_SELECTOR, 'input[name="closed-quantity"]')
    USED_QUANTITY = (By.CSS_SELECTOR, 'input[name="used-quantity"]')
    MESSAGE = (By.CSS_SELECTOR, 'textarea[name="message"]')
    RADIO_DEFECT = (By.CSS_SELECTOR, '#reklamForm > form > div.body > div:nth-child(19) > div:nth-child(3) > label')
    RADIO_REQUIREMENT = (By.CSS_SELECTOR, '#reklamForm > form > div.body > div:nth-child(20) > div:nth-child(3) > label')

    INPUT_FILE = (By.CSS_SELECTOR, 'div[class="input-wrap"] input[type="file"]')

class CallbacklLocators:

    BUTTON_CALL = (By.CSS_SELECTOR, 'a[class="callback2order top-callback transition header-callback"]')
    NAME = (By.CSS_SELECTOR, '#callbackOrderForm > form > div.body > div:nth-child(1) > input[type=text]')
    NUMBER = (By.CSS_SELECTOR, '#callbackOrderForm > form > div.body > div:nth-child(2) > input[type=text]')
    BUTTON_SEND = (By.CSS_SELECTOR, '#callbackOrderForm > form > div.footer > button')

class SearchImageLocators:

    NAME = (By.CSS_SELECTOR, 'input[id="name"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="email"]')
    CITY = (By.CSS_SELECTOR, 'input[id="city_name"]')
    MESSAGE = (By.CSS_SELECTOR, 'textarea[id="message"]')

    BUTTON_ADD_FILE = (By.CSS_SELECTOR, 'input[class="js_file"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'div[class="send_button js_send_form"]')

    #output files

    TEXT_FILE = (By.CSS_SELECTOR, 'div[class="input_file_blocks"] div[class="js_selected_files"]:nth-child(2)')

class SelectionByParametersLocators:
    BUTTON_SEND_1 = (By.CSS_SELECTOR, 'div[class="row js_to_podbor_form"] div[class="pf_button"]')
    NAME = (By.CSS_SELECTOR, 'form[name="podborinlistform"] input[name="name"]')
    PHONE = (By.CSS_SELECTOR, 'form[name="podborinlistform"] input[name="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'form[name="podborinlistform"] input[name="email"]')
    BUTTON_SEND_2 = (By.CSS_SELECTOR, 'form[name="podborinlistform"] button[class="btn"] ')



class FormOrderOneClickLocators:
    BUTTON_ONE_CLICK = (By.CSS_SELECTOR, 'div:nth-child(12) [class="fast-button-list"] a[class="quick2order fast__order"]')
    PRICE = (By.CSS_SELECTOR, 'span[class="is_price js_price"]')
    BUTTON_INCREASE = (By.CSS_SELECTOR, 'div[class="count_plus js_count_plus"]')
    #input data
    NAME = (By.CSS_SELECTOR, 'div[id="colorbox"] div[class="body"] input[name="name"]')
    PHONE = (By.CSS_SELECTOR, 'div[id="colorbox"] div[class="body"] input[name="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'div[id="colorbox"] div[class="body"] input[name="email"]')
    MESSAGE = (By.CSS_SELECTOR, 'div[id="colorbox"] div[class="body"] textarea[name="message"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'div[id="cboxContent"] div[class="footer"] button[class="btn"]')

class FormSelectionPaintBannerLocators:
    BUNNER = (By.CSS_SELECTOR, 'li[class="top_submenu_banner_block js_top_submenu_banner"]')
    NAME = (By.CSS_SELECTOR, 'input[id="name"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="email"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'div[class="submit_wrap"] button[type="submit"]')


class FormSpecialPriceLocators:
    BUTTON_SPECIAL_PRICE = (By.CSS_SELECTOR, 'a[data-url="/catalog/morris-co-arhive/112850/"]')
    NAME = (By.CSS_SELECTOR, 'form[name="specpriceorderform"] input[name="name"]')
    PHONE = (By.CSS_SELECTOR, 'form[name="specpriceorderform"] input[name="phone"]')
    EMAIL = (By.CSS_SELECTOR, 'form[name="specpriceorderform"] input[name="email"]')
    MESSAGE = (By.CSS_SELECTOR, 'form[name="specpriceorderform"] textarea[name="comment"]')
    CALLS_FROM = (By.CSS_SELECTOR, 'div[class="time_of_call"] input[name="time_from"]')
    CALLS_TO = (By.CSS_SELECTOR, 'div[class="time_of_call"] input[name="time_to"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'div[class="footer"] input[type="submit"]')

class FormFoundCheaperLocators:
    BUTTON_FOUND_CHEAPER = (By.CSS_SELECTOR, 'div[class="do-discount"]')
    NAME = (By.CSS_SELECTOR, 'div[class="form_content"] input[name="best_name"]')
    PHONE = (By.CSS_SELECTOR, 'div[class="form_content"] input[name="best_phone"]')
    EMAIL = (By.CSS_SELECTOR, 'div[class="form_content"] input[name="best_email"]')
    PRICE = (By.CSS_SELECTOR, 'div[class="form_content"] input[name="best_price"]')
    LINK = (By.CSS_SELECTOR, 'div[class="form_content"] input[name="best_link"]')
    BUTTON_SEND = (By.CSS_SELECTOR, 'div[class="form_content"] input[type="submit"]')

class FormCalculatorLocators:
    PRICE_ONE = (By.CSS_SELECTOR, 'span[class="js_price"]')

    BUTTON_CALCULATOR = (By.CSS_SELECTOR, 'div[class="calc-count"] a[class="calc-fancybox"]')
    HEIGHT = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__walls div:nth-child(1) input[type=text]')
    WALL_1 = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__walls > div:nth-child(2) input[type=text]')
    WALL_2 = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__walls > div:nth-child(3) input[type=text]')
    WALL_3 = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__walls > div:nth-child(4) input[type=text]')
    WALL_4 = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__walls > div:nth-child(5) input[type=text]')
    DOOR = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__doors input[type=text]')
    WINDOW = (By.CSS_SELECTOR, 'div.walls-wrap.walls-wrap__windows input[type=text]')
    BUTTON_RESULT = (By.CSS_SELECTOR, 'a[class="btn-yellow"]')
    PERIMETR_RESULT = (By.CSS_SELECTOR, 'div[class="col-xs-3"] span[class="results"]')
    NUMBERS_OF_ROLLS = (By.CSS_SELECTOR, 'div[class="col-xs-4"] span[class="results"]')
    PRICE_SUMMA = (By.CSS_SELECTOR, 'div[class="col-xs-2 price_block"]')
