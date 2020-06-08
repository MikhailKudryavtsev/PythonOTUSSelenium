
def test_otus(remote2):
    remote2.get('https://otus.ru/')
    assert 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям' in remote2.title


def test_wikipedia(remote2):
    remote2.get('https://google.ru')
    assert remote2.title == 'Google'


def test_yandex(remote2):
    remote2.get('https://ya.ru')
    remote2.find_element_by_css_selector('button.button').click()
    assert remote2.title == 'Яндекс: задан пустой поисковый запрос'
