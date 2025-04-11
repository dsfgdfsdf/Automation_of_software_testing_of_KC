def test_opencart_iphone(driver):
    driver.goto(
        "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=24",
        timeout=60000  
    )

    search_box = driver.locator("input[name='search']")
    search_box.fill("iPhone")
    search_box.press("Enter")

    
    driver.locator("div.product-thumb").wait_for()
    product_titles = driver.locator("div.product-thumb h4 a").all_text_contents()
    
    assert any("iPhone" in title for title in product_titles)
