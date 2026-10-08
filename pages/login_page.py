from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage, retry_on_popup


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.login_email = (By.NAME, "email")
        self.login_password = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[data-qa='login-button']")

        self.signup_name = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
        self.signup_email = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
        self.signup_button = (
            By.CSS_SELECTOR, "button[data-qa='signup-button']")

    @retry_on_popup()
    def login(self, email, password):
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.login_email)
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.driver.find_element(*self.login_password)
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element(*self.login_button).click()

    @retry_on_popup()
    def signup(self, name, email):
        name_input = self.wait.until(
            EC.element_to_be_clickable(self.signup_name)
        )

        name_input.clear()
        name_input.send_keys(name)

        email_input = self.driver.find_element(*self.signup_email)
        email_input.clear()
        email_input.send_keys(email)

        self.driver.find_element(*self.signup_button).click()

    def get_email_validation(self):
        email_input = self.driver.find_element(*self.signup_email)

        message = self.driver.execute_script(
            "return arguments[0].validationMessage;", email_input
        )

        return message
