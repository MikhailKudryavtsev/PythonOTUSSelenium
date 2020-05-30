from selenium.webdriver.common.by import By


class Locators:

    input_username = (By.CSS_SELECTOR, 'input#input-username')
    input_password = (By.CSS_SELECTOR, 'input#input-password')
    button_login = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    catalog = (By.XPATH, '//*[@id="menu-catalog"]/a')
    products = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    button_add_product = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    input_product_name = (By.CSS_SELECTOR, 'input#input-name1')
    input_meta_title = (By.CSS_SELECTOR, 'input#input-meta-title1')
    input_model = (By.CSS_SELECTOR, 'input#input-model')
    tbody_tr_products = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr')
    button_save_products = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
    footer = (By.ID, 'footer')
    panel_title = (By.CLASS_NAME, 'panel-title')
    link_OpenCart = (By.LINK_TEXT, 'OpenCart')
    button_search = (By.XPATH, '//*[@id="search"]/span/button')
    navbar = (By.CSS_SELECTOR, 'ul.nav.navbar-nav')
    left_column = (By.ID, 'column-left')
    swiper_viewport = (By.CLASS_NAME, 'swiper-viewport')
    link_Desktops = (By.LINK_TEXT, 'Desktops')
    form_product = (By.CSS_SELECTOR, 'form#form-product')
    img_user_profile = (By.CSS_SELECTOR, 'img#user-profile.img-circle')
    buttom_logout = (By.XPATH, '//*[@id="header"]/div/ul/li[2]/a')
    panel_heading = (By.CSS_SELECTOR, 'h1.panel-title')
    list_group = (By.XPATH, '//*[@id="column-right"]/div')
    button_Continue = (By.CSS_SELECTOR, 'a.btn.btn-primary')
    container_account_login = (By.ID, 'account-login')
    navbar_header = (By.CLASS_NAME, 'navbar-header')
    link_Forgotten_Password = (By.LINK_TEXT, 'Forgotten Password')
    h1_device_name = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    button_add_card = (By.CSS_SELECTOR, 'button#button-cart')
    container_product = (By.ID, 'product-product')
    nav_tabs = (By.CLASS_NAME, 'nav-tabs')
    button_remove_product = (By.CSS_SELECTOR, 'button.btn.btn-danger')
    your_store = (By.XPATH, '//*[@id="logo"]/h1/a')
    button_cart = (By.CSS_SELECTOR, '.btn-group.btn-block')
    form_currency = (By.ID, 'form-currency')
    list_buttons = (By.CLASS_NAME, 'list-inline')
    link_MacBook = (By.LINK_TEXT, 'MacBook')
    input_prod_name_filer = (By.CSS_SELECTOR, 'input#input-name')
    buttom_filter = (By.CSS_SELECTOR, 'button#button-filter')
    cart_dropdown_menu = (By.CSS_SELECTOR, 'ul.dropdown-menu.pull-right')
    input_search = (By.CSS_SELECTOR, 'input.form-control.input-lg')
    search_results = (By.CSS_SELECTOR, 'div.col-sm-12')
    form_Forgotten_Password = (By.CSS_SELECTOR, 'div.panel.panel-default')