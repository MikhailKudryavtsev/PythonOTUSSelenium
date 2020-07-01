import pymysql

class DBmanager:

    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            database='bitnami_opencart',
            port=88,
            user='bn_opencart',
            password=''
        )
        self.cursor = self.connect.cursor()

    def close_connect(self):
        self.cursor.close()
        self.connect.close()

    def create_product(self, id_, product):
        data = (f'{id_}', '1', f'{product}', '', '', 'Test', '', '')
        query1 = f"INSERT INTO oc_product_description " \
                 f"(product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword) VALUES {data}"

        data = (f'{id_}', 'TestModel', '', '', '', '', '', '', '', '5', '5', '', '0', '1', '999', '0', '9', '2009-02-08', '2009-02-10')
        query2 = f"INSERT INTO oc_product (product_id, model, sku, upc, ean, jan, isbn, mpn, location, quantity, " \
                 f"stock_status_id, image, manufacturer_id, shipping, price, points, tax_class_id, date_added, date_modified) " \
                 f"VALUES {data}"

        self.cursor.execute(query1)
        self.cursor.execute(query2)
        self.connect.commit()

    def check_product(self, product_name):
        query = f"SELECT * from oc_product_description WHERE name='{product_name}'"
        self.cursor.execute(query)
        self.connect.commit()
        self.product_in_db = self.cursor.fetchone()

    def update_product(self, name, id_):
        query = f"UPDATE oc_product_description SET name='{name}' WHERE product_id={id_}"
        self.cursor.execute(query)
        self.connect.commit()
        self.product_in_db = self.cursor.fetchone()

    def delete_product(self, id_):
        query1 = f"DELETE FROM oc_product_description WHERE product_id={id_}"
        query2 = f"DELETE FROM oc_product WHERE product_id={id_}"
        self.cursor.execute(query1)
        self.connect.commit()
        self.product_in_oc_product_description = self.cursor.fetchone()
        self.cursor.execute(query2)
        self.connect.commit()
        self.product_in_oc_product = self.cursor.fetchone()
