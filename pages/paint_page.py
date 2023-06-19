import random

from pages.base_page import BasePage
from locators.paint_locators import PaintLocators



class PaintPage(BasePage):
    locators = PaintLocators()

    """Сравнение свойств в фильтре и фактичекской выдачи"""
    def comparison_of_destination_properties(self):
        wall = self.locators.FLAG_WALL
        ceiling = self.locators.FLAG_CEILING
        furniture = self.locators.FLAG_FURNITURE
        floor = self.locators.FLAG_FLOOR
        wallpaper = self.locators.FLAG_WALLPAPER
        facade = self.locators.FLAG_FACADE
        radiators = self.locators.FLAG_RADIATORS
        plintch = self.locators.FLAG_PLINTH
        roof = self.locators.FLAG_ROOF

        destination = {1:wall, 2:ceiling, 3:furniture, 4:floor, 5:floor,
                       6:wallpaper, 7:facade, 8:radiators, 9:plintch, 10:roof}

        self.elements_is_clickable(destination[random.randint(1,10)]).click()


    def click_icon_whatsapp(self):
        self.elements_is_clickable(self.locators.BUTTON_WHATSAPP).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        promokod = self.elements_is_present(self.locators.PROMOKOD_TEXT).text
        print(f'Промокод: {promokod.split()[-1]}')


    def choose_a_gloss(self):
        self.elements_is_clickable(self.locators.BUTTON_GLOSS).click()
        self.elements_is_clickable(self.locators.FLAG_GLOSS).click()

    def reset_everything(self):
        self.elements_is_clickable(self.locators.BUTTON_RESET).click()

    def choosing_the_basis(self):
        self.elements_is_clickable(self.locators.BUTTON_BASIS).click()
        self.elements_is_clickable(self.locators.FLAG_BASIS).click()