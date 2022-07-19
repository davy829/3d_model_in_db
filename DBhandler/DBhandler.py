import sqlite3

class DBHandler():
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # Получить все элементы из таблицы
    def getItems(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table};')
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print('Ошибка чтения из БД', e)
        return []

    # Добавить элемент в таблицу
    def addItem(self, table, args):
        items = ','.join(["'" + str(field) + "'" for field in args])
        print(items, " ", table)
        try:
            self.__cur.execute(f"INSERT INTO {table} VALUES ({items});")
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления записи в БД', e)
            return False
        return True

    # Получить элемент в таблице по ID
    def getItemById(self, table, id):
        try:
            self.__cur.execute(f"SELECT * FROM {table} WHERE ID = {id} LIMIT 1;")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения записи из БД', e)
        return False

    # Удалить элемент по ID
    def deleteItemById(self, table, id):
        print(id, " ", table)
        try:
            self.__cur.execute(f"DELETE FROM {table} WHERE ID = {id};")
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления записи из БД', e)
            return False
        return True

    # Обновить элемент по ID
    def updateItemById(self, table, value, id):
        print(id, " ", table, " ", value)
        try:
            self.__cur.execute(f"UPDATE {table} set Description = '{value}' WHERE ID = {id};")
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления записи из БД', e)
            return False
        return True

    # Получить элемент по значению поля
    def getItemByField(self, table, field, value):
        try:
            self.__cur.execute(f"SELECT * FROM {table} WHERE {field} = '{value}' LIMIT 1;")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения записи из БД', e)
        return False