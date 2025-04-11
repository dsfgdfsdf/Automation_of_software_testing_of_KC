def test_auth_page(driver):
    driver.goto("https://testpages.eviltester.com/styled/auth/basic-auth-test.html")

    username_text = driver.locator("//p[contains(text(), 'username:')]").inner_text()
    password_text = driver.locator("//p[contains(text(), 'password:')]").inner_text()
    username = username_text.split(": ")[1]
    password = password_text.split(": ")[1]

    assert driver.locator("//a[contains(text(), 'Basic Auth')]").is_visible()

    auth_url = f"https://{username}:{password}@testpages.eviltester.com/styled/auth/basic-auth-results.html"
    driver.goto(auth_url)

    assert driver.locator("//span[contains(text(), 'Authenticated')]").is_visible()
