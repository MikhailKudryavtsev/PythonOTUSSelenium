import time

from selenium.webdriver.common.keys import Keys


def test_wikipedia(remote):
    remote.get('https://google.ru')
    remote.find_element_by_css_selector('input.gLFyf.gsfi').send_keys('wikipedia')
    remote.find_element_by_css_selector('input.gLFyf.gsfi').send_keys(Keys.ENTER)
    time.sleep(5)   # Из-за дойгой загрузки на VM
    assert remote.title == 'wikipedia - Поиск в Google'


def test_yandex(remote):
    remote.get('https://ya.ru')
    remote.find_element_by_css_selector('button.button').click()
    time.sleep(5)   # Из-за дойгой загрузки на VM
    assert remote.title == 'Яндекс: задан пустой поисковый запрос'


def test_otus(remote):
    remote.get('https://otus.ru/')
    assert 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям' in remote.title
