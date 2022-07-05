from DBhandler.DBhandler import DBHandler

#Базовый класс модели
class BaseModel():

    table = 'BASETABLE'

    # Получить все записи для модели
    @staticmethod
    def getAll(table: str, dbhandler: DBHandler) -> list:
        return dbhandler.getItems(table)

    # Получить элемент модели по ID
    @staticmethod
    def getItemByID(table: str, id: int, dbhandler: DBHandler) -> tuple:
        return dbhandler.getItemById(table, id)

    # Удалить элемент модели по ID
    @staticmethod
    def deleteItemByID(table: str, id: int, dbhandler: DBHandler) -> bool:
        return dbhandler.deleteItemById(table, id)

    # Добавить элемент 
    def addItem(self, dbhandler: DBHandler) -> bool:
        return dbhandler.addItem(self.table, self.getAllFields())

    # Получить все поля объекта для его сериализации
    def getAllFields(self):
        return ()
    


    


