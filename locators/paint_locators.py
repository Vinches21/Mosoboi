from selenium.webdriver.common.by import By
import random as r


class PaintLocators:
    #checbox назначение краски
    FLAG_WALL = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                                  'div.row.bx-filter-parameters-box-container > div > div:nth-child(1) > label:nth-child(1)')

    FLAG_CEILING = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(2) > label:nth-child(1)')

    FLAG_FURNITURE = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(3) > label:nth-child(1)')

    FLAG_FLOOR = ( By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(4) > label:nth-child(1)')

    FLAG_WALLPAPER = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(5) > label:nth-child(1)')

    FLAG_FACADE = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(6) > label:nth-child(1)')

    FLAG_RADIATORS = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(7) > label:nth-child(1)')

    FLAG_PLINTH = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(8) > label:nth-child(1)')

    FLAG_ROOF = (By.CSS_SELECTOR, 'div.NAZNACHENIE.col-lg-12.bx-filter-parameters-box.bx-active > div.bx-filter-block > '
                     'div.row.bx-filter-parameters-box-container > div > div:nth-child(9) > label:nth-child(1)')

    #output
    OUTPUT_WALL = (By.CSS_SELECTOR, 'div[class="item"]')

    # degree of gloss степень блеска

    BUTTON_GLOSS = (By.CSS_SELECTOR, 'div.STEPEN_BLESKA.col-lg-12.bx-filter-parameters-box > div.bx-filter-parameters-box-title.bx-not-active')

    FLAG_GLOSS = (By.CSS_SELECTOR, f'div.STEPEN_BLESKA.col-lg-12.bx-filter-parameters-box > div.bx-filter-block > '
                                   f'div.row.bx-filter-parameters-box-container > div > div.filter-primary-list > div:nth-child({r.randint(1, 5)})')

    #reset
    BUTTON_RESET = (By.CSS_SELECTOR, '#del_filter')


    #basis

    BUTTON_BASIS = (By.CSS_SELECTOR, 'div.OSNOVA.col-lg-12.bx-filter-parameters-box > div.bx-filter-parameters-box-title.bx-not-active')
    FLAG_BASIS = (By.CSS_SELECTOR, 'div.OSNOVA.col-lg-12.bx-filter-parameters-box > div.bx-filter-block'
                                   ' > div.row.bx-filter-parameters-box-container > div > div:nth-child(2) > label:nth-child(1)')


    #icon whatsapp

    BUTTON_WHATSAPP = (By.CSS_SELECTOR, 'body > div.uw-widget > ul > li.whatsapp > a')
    PROMOKOD_TEXT = (By.CSS_SELECTOR, '#main_block > p')
