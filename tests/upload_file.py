import os


def test_upload_file(driver):
    url = 'https://mdn.mozillademos.org/ru/docs/Web/HTML/Element/Input/file$samples/Limiting_accepted_file_types?revision=1603567'
    driver.get(url)
    dirname = os.path.dirname(__file__)
    file = '1.png'
    filename = os.path.join(dirname, file)
    item = driver.find_element_by_css_selector('input#profile_pic')
    item.send_keys(filename)
    assert file in item.get_attribute("value"), 'Файл не загружен'
