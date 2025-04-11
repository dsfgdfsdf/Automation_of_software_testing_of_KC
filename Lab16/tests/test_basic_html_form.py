def test_basic_html_form(driver):
    import os
    import time

    driver.goto("https://testpages.eviltester.com/styled/basic-html-form-test.html")

    username_input = "mukola"
    password_input = "mukolaasdfghjkl"
    comments_input = "this is a comment box"
    file_upload = os.path.abspath("file_test_barda.txt")

    driver.locator("input[name='username']").fill(username_input)
    driver.locator("input[name='password']").fill(password_input)
    driver.locator("textarea[name='comments']").fill(comments_input)

    driver.locator("input[name='filename']").set_input_files(file_upload)

    driver.locator("input[value='cb1']").check()
    driver.locator("input[value='cb3']").check()

    driver.locator("input[value='rd2']").check()

    multi_select = driver.locator("select[name='multipleselect[]']")
    multi_select.select_option("ms3")

    driver.locator("select[name='dropdown']").select_option("dd6")

    driver.locator("input[type='submit']").click()


    driver.wait_for_url("**/the_form_processor.php")
    assert "the_form_processor.php" in driver.url
