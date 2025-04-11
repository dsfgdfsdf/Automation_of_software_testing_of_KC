from time import sleep

def test_dynamic_buttons_flow(driver):
    driver.goto("https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html")

    driver.locator("#button00").click()
    driver.locator("#button01").click()
    driver.locator("#button02").click()
    driver.locator("#button03").click()

    message = driver.locator("#buttonmessage")
    assert message.inner_text() == "All Buttons Clicked"
