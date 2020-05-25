

def test_check_cart(start_page):
    start_page.open_cart()
    assert 'Your shopping cart is empty!' in start_page.cart_menu.get_attribute('textContent'), 'Корзина не пуста.'
