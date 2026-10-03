from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.automationexercise.com")
# print(driver.title)
wait = WebDriverWait(driver, 10)


def click_on(params):
    element = driver.find_element(*params)
    if element.is_displayed() and element.is_enabled():
        element.click()


def clear_popup(driver=driver):
    iframes = driver.find_elements(
        By.CSS_SELECTOR, 'iframe[title="Advertisement"]')

    for iframe in iframes:
        if iframe.is_displayed():
            try:
                driver.switch_to.frame(iframe)

                close_button = driver.find_element(
                    By.CLASS_NAME, "continue-prompt-text")
                close_button.click()
            except:
                pass
            finally:
                driver.switch_to.default_content()

    return


while True:
    try:
        click_on((By.XPATH, "//a[@href='/products']"))
    except:
        clear_popup()
        continue

    try:
        click_on((By.XPATH, "//a[@href='/']"))
    except:
        clear_popup()
        continue

# input()
# driver.quit()
