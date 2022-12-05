import typing
import psycopg2
from queries import *


class SQLManager:

    def __init__(self, dbname, user, password, host='localhost'):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute(CREATE_TABLES_QUERY)
        self.connection.commit()

    def insert_data(self):
        self.cursor.execute(INSERT_INTO_TABLES_QUERY)
        self.connection.commit()

    def select_data(self, num: float) -> typing.Tuple[typing.Tuple[str]]:
        if num == 3.1:
            self.cursor.execute(QUERY_3_1)
            return self.cursor.fetchall()
        if num == 3.2:
            self.cursor.execute(QUERY_3_2)
            return self.cursor.fetchall()
        if num == 3.3:
            self.cursor.execute(QUERY_3_3)
            return self.cursor.fetchall()
        if num == 3.4:
            self.cursor.execute(QUERY_3_4)
            return self.cursor.fetchall()
        if num == 3.5:
            self.cursor.execute(QUERY_3_5)
            return self.cursor.fetchall()
        if num == 3.6:
            self.cursor.execute(QUERY_3_6)
            return self.cursor.fetchall()
        if num == 3.7:
            self.cursor.execute(QUERY_3_7)
            return self.cursor.fetchall()
        if num == 3.8:
            self.cursor.execute(QUERY_3_8)
            return self.cursor.fetchall()
        if num == 3.9:
            self.cursor.execute(QUERY_3_9)
            return self.cursor.fetchall()
        if num == 3.10:
            self.cursor.execute(QUERY_3_10)
            return self.cursor.fetchall()
        if num == 3.11:
            self.cursor.execute(QUERY_3_11)
            return self.cursor.fetchall()
        if num == 3.12:
            self.cursor.execute(QUERY_3_12)
            return self.cursor.fetchall()
        if num == 3.13:
            self.cursor.execute(QUERY_3_13)
            return self.cursor.fetchall()

    def update_data(self):
        self.cursor.execute("UPDATE Items SET price = price + 100 WHERE name ILIKE '%e' OR name ILIKE 'b%' ")

    def delete_data(self, num: float):
        if num == 5.1:
            self.cursor.execute(QUERY_5_1)
        if num == 5.2:
            self.cursor.execute(QUERY_5_2)
        if num == 5.3:
            self.cursor.execute(QUERY_5_3)
        if num == 5.4:
            self.cursor.execute(QUERY_5_4)

    def drop_tables(self):
        self.cursor.execute("DROP TABLE Shops, Departments, Items;")
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


instance = SQLManager(dbname='', user='', password='')
instance.drop_tables()
instance.create_tables()
instance.insert_data()
print(instance.select_data(3.7))
instance.delete_data(5.2)
instance.update_data()
instance.close_connection()
