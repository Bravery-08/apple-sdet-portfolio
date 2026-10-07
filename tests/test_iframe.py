from pages.the_internet.iframe import Iframe

def test_iframe_switches(driver):
    driver.get('https://the-internet.herokuapp.com/iframe')
    
    page=Iframe(driver)
    page.click_close()
    
    driver.switch_to.frame(page.get_iframe())
    message=page.get_message()
    driver.switch_to.default_content()
    
    assert message=='Your content goes here.'