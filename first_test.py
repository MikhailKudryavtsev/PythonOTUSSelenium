

def test_opencart(url, driver):
    driver.get(url)
    assert driver.title == 'Your Store'
