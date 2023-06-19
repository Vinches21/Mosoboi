from  selenium.webdriver.common.by import By


class CartLocators:
    TITLE_FACTORY = (By.CSS_SELECTOR, 'div.name_b_item.col-xs-12.col-sm-4')

    BUTON_PLACE_ORDER = (By.CSS_SELECTOR, 'a[class="checkout oform_b"]')

    BUTTON_INCREASE = (By.CSS_SELECTOR, 'input[class="disthis plus"]')
    BUTTON_REDUCE = (By.CSS_SELECTOR, 'input[class="disthis minus"]')
    DELETE_PRODUCT = (By.CSS_SELECTOR, 'a[class="delete-item"]')

    #message
    CART_EMPTY = (By.CSS_SELECTOR, 'div[class="errortext"]')