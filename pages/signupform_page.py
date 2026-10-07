from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage, retry_on_popup


class SignupformPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.country = (By.CSS_SELECTOR, "select#country")

    @retry_on_popup()
    def select_country(self, country):
        country_select = Select(self.driver.find_element(*self.country))
        country_select.select_by_visible_text(country)

    @retry_on_popup()
    def get_country(self):
        country_select = Select(self.driver.find_element(*self.country))
        return country_select.first_selected_option.text
