
def test_click_YourStore(start_page):
    start_page.get_url()
    start_page.find_element(start_page.driver, start_page.your_store).click()
    assert start_page.driver.current_url == f'{start_page.url}index.php?route=common/home', 'Открылась другая страница'
