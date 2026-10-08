from pages.the_internet.js_alerts import JS_alerts


def test_js_works(driver):
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    page = JS_alerts(driver)

    page.click_alert()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

    page.click_confirm()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()

    page.click_prompt()
    alert = driver.switch_to.alert
    alert.send_keys('Shaurya')
    alert.accept()

    assert 'Shaurya' in page.get_result()
