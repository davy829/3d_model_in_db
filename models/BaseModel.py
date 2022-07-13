from DBhandler.DBhandler import DBHandler

#Базовый класс модели
class BaseModel():

    @staticmethod
    def get_table():
        return "Basemodel"

    # Получить все записи для модели
    @staticmethod
    def getAll(dbhandler: DBHandler) -> list:
        return dbhandler.getItems(BaseModel.get_table())

    # Получить элемент модели по ID
    def getItemByID(self, id: int, dbhandler: DBHandler) -> tuple:
        return dbhandler.getItemById(type(self).get_table(), id)

    # Удалить элемент модели по ID
    def deleteItemByID(self, id: int, dbhandler: DBHandler) -> bool:
        return dbhandler.deleteItemById(type(self).get_table(), id)

    # Добавить элемент 
    def addItem(self, dbhandler: DBHandler) -> bool:
        return dbhandler.addItem(type(self).get_table(), self.getAllFields())

    # Получить все поля объекта для его сериализации
    def getAllFields(self):
        return ()
    


    


