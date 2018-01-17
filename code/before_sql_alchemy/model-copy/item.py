import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name)

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        @classmethod
        def update(cls, item):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
            cursor.execute(query, (item['price'], item['name']))

            connection.commit()
            connection.close()
