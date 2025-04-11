import os

def test_file_upload(driver):
    driver.goto("https://testpages.eviltester.com/styled/file-upload-test.html")

    file_path = os.path.abspath("file_test_barda.txt")
    file_name = os.path.basename(file_path)

    driver.locator("input[name='filename']").set_input_files(file_path)
    driver.locator("#itsafile").click()
    driver.locator("input[name='upload']").click()

    assert driver.locator(f"//p[contains(text(), '{file_name}')]").is_visible()
