from DBhandler.DBhandler import DBHandler

#Базовый класс модели
class BaseModel():

    table = 'BASETABLE'

    # Получить все записи для модели
    def getAll(self, dbhandler: DBHandler) -> list:
        return dbhandler.getItems(self.table)

    # Получить элемент модели по ID
    def getItemByID(self, id: int, dbhandler: DBHandler) -> tuple:
        return dbhandler.getItemById(self.table, id)

    # Удалить элемент модели по ID
    def deleteItemByID(self, id: int, dbhandler: DBHandler) -> bool:
        return dbhandler.deleteItemById(self.table, id)

    # Добавить элемент 
    def addItem(self, dbhandler: DBHandler) -> bool:
        return dbhandler.addItem(self.table, self.getAllFields())

    # Получить все поля объекта для его сериализации
    def getAllFields(self):
        return ()
    


    


