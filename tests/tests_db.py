import time


def test_add_product_in_db(db_manager):
    product_name = 'TestProduct'
    id_ = '50'
    db_manager.create_product(id_, product_name)
    time.sleep(1)
    db_manager.check_product(product_name)
    db_manager.close_connect()
    assert product_name in db_manager.product_in_db, "Продукт не создан"


def test_remove_product_in_db(db_manager):
    product_name = 'TestProduct'
    id_ = '52'
    db_manager.create_product(id_, product_name)
    db_manager.delete_product(id_)
    time.sleep(1)
    db_manager.check_product(product_name)
    db_manager.close_connect()
    assert db_manager.product_in_oc_product_description == None and \
           db_manager.product_in_oc_product == None, "Продукт не удален"


def test_product_change_in_db(db_manager):
    product_name = 'TestProduct'
    id_ = '51'
    name = 'NewNameTestProduct'
    db_manager.create_product(id_, product_name)
    db_manager.update_product(name, id_)
    time.sleep(1)
    db_manager.check_product(name)
    db_manager.close_connect()
    assert name in db_manager.product_in_db, "Продукт не изменен"


def test_add_product_in_web(db_manager, product):
    product.create_product()
    time.sleep(1)
    db_manager.check_product(product.random_name)
    db_manager.close_connect()
    assert product.random_name in db_manager.product_in_db, "Продукт не создан"


def test_remove_product_in_web(db_manager, product):
    product.remove_product()
    time.sleep(1)
    db_manager.check_product(product.random_name)
    db_manager.close_connect()
    assert db_manager.product_in_db == None, "Продукт не удален"


def test_product_change_in_web(db_manager, product):
    product.product_change()
    # time.sleep(1)
    db_manager.check_product(product.new_name)
    db_manager.close_connect()
    assert product.new_name in db_manager.product_in_db, "Продукт не изменен"
