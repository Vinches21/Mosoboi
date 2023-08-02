from selenium.webdriver.common.by import By


class OrderLocators:
    #data
    PRIVATE_PERSON = (By.CSS_SELECTOR, 'input[id="PERSON_TYPE_1"]')
    COMPANY = (By.CSS_SELECTOR, 'input[id="PERSON_TYPE_2"]')

    NAME = (By.CSS_SELECTOR, 'input[id="ORDER_PROP_1"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="ORDER_PROP_2"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="ORDER_PROP_3"]')
    CITY = (By.CSS_SELECTOR, 'input[id="ORDER_PROP_6"]')
    ADDRESS = (By.CSS_SELECTOR, 'textarea[id="ORDER_PROP_7"]')
    COMMENT = (By.CSS_SELECTOR, 'textarea[id="ORDER_DESCRIPTION"]')

    #delivery method
    DELIVERY_IN_MOSCOW = (By.CSS_SELECTOR, 'div[class="item_oform_z_text"] label[for="ID_DELIVERY_ID_1"]')
    CDEK = (By.CSS_SELECTOR, 'div[class="item_oform_z_text"] label[for="ID_DELIVERY_ID_60"]')
    LENINSKIY_24 = (By.CSS_SELECTOR, 'div.item_oform_z.id_24 > label')
    VOYKOVSKAYA = (By.CSS_SELECTOR, 'div.item_oform_z.id_23 > label')
    GOVOROVO = (By.CSS_SELECTOR, 'div.item_oform_z.id_61 > label')
    AVTOZAVODSKAYA = (By.CSS_SELECTOR, 'div.item_oform_z.id_2 > label')
    TERMINAL_TRANSPORT = (By.CSS_SELECTOR, 'div.item_oform_z.id_3 > label')
    FLAT_TRANSPORT = (By.CSS_SELECTOR, 'div.item_oform_z.id_4 > label')

    #payment system

    CASH = (By.CSS_SELECTOR, '#paysystem_ico_1')
    SBERBANK = (By.CSS_SELECTOR, '#paysystem_ico_9')
    ONLINE_PAYMENT = (By.CSS_SELECTOR, '#paysystem_ico_14')
    CREDIT = (By.CSS_SELECTOR, '#paysystem_ico_10')
    BANK_TRANSFER = (By.CSS_SELECTOR, '#paysystem_ico_7')


    #sealer

    BUTTON_SEALER = (By.CSS_SELECTOR, '.js_withHelp')
    BUTTON_SELECT = (By.CSS_SELECTOR, '#ORDER_PROP_30')

    #oform

    BUTTON_ORDER = (By.CSS_SELECTOR, 'a[class="oform_b js-form-add-new-order"]')