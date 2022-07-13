from DBhandler.DBhandler import DBHandler

#Базовый класс модели
class BaseModel():

    @staticmethod
    def get_table():
        return "Basemodel"

    def get_id(self):
        pass

    # Получить все записи для модели
    @staticmethod
    def getAll(dbhandler: DBHandler) -> list:
        return dbhandler.getItems(BaseModel.get_table())

    # Получить элемент модели по ID
    def getItemByID(self, dbhandler: DBHandler) -> tuple:
        return dbhandler.getItemById(type(self).get_table(), self.get_id())

    # Удалить элемент модели по ID
    def deleteItemByID(self, dbhandler: DBHandler) -> bool:
        return dbhandler.deleteItemById(type(self).get_table(), self.get_id())

    # Добавить элемент 
    def addItem(self, dbhandler: DBHandler) -> bool:
        return dbhandler.addItem(type(self).get_table(), self.getAllFields())

    # Получить все поля объекта для его сериализации
    def getAllFields(self):
        return ()
    
    
    


    


