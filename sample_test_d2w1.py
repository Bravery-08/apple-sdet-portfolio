from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

while True:

    driver = webdriver.Chrome()
    driver.get("https://www.automationexercise.com")
    # print(driver.title)
    wait=WebDriverWait(driver,10)

    def clear_popup(driver=driver):
        try:
            popup=WebDriverWait(driver,3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "continue-prompt-text"))
            )
            popup.click()
        except TimeoutException:
            pass
        
        return
        
    #1
    loginbutton=driver.find_element(By.XPATH,"//a[@href='/login']")
    print(loginbutton.text)

    clear_popup()

    #2
    products=driver.find_element(By.XPATH,"//a[@href='/products']")
    products.click()

    clear_popup()

    print("URL:", driver.current_url)
    print("TITLE:", driver.title)

    # need to wait for accessing elements after loading new page
    search=wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    print(search.get_attribute("placeholder"))

    clear_popup()

    #3
    home=driver.find_element(By.XPATH, "//a[@href='/']")
    home.click()

    clear_popup()

    product_card=wait.until(
        EC.presence_of_element_located((By.XPATH,"//img[@src='/get_product_picture/1']/following-sibling::p"))
    )
    print(product_card.text)

    clear_popup()

    #4
    cart=driver.find_element(By.XPATH, "//a[@href='/view_cart']")
    print(cart.text)

    # input()
    driver.quit()