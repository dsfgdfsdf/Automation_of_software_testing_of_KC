def test_simple_alert(driver):
    driver.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

    def handle_dialog(dialog):
        dialog.accept()

    driver.once("dialog", handle_dialog)

    driver.locator("#alertexamples").click()

    assert "triggered and handled the alert dialog" in driver.locator("#alertexplanation").inner_text()
