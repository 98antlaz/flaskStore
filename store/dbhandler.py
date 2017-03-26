import sqlite3

class dbhandler:
    def __init__(self):
        self.connection = sqlite3.connect("storage.db")
        self.cursor = self.connection.cursor()

    def getProducts(self):
        sql = "SELECT * FROM products"
        self.cursor.execute(sql)
        fetched = self.cursor.fetchall()
        products = []
        for tup in fetched:
            products.append(list(tup))
        return products
