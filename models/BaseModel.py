from DBhandler.DBhandler import DBHandler

#Базовый класс модели
class BaseModel():

    table = 'BASETABLE'

    # Получить все записи для модели
    @staticmethod
    def getAll(table: str, controller: DBHandler) -> list:
        return controller.getItems(table)

    # Получить элемент модели по ID
    @staticmethod
    def getItemByID(table: str, id: int, controller: DBHandler) -> tuple:
        return controller.getItemById(table, id)

    # Удалить элемент модели по ID
    @staticmethod
    def deleteItemByID(table: str, id: int, controller: DBHandler) -> bool:
        return controller.deleteItemById(table, id)

    # Добавить элемент 
    def addItem(self, controller: DBHandler):
        return controller.addItem(self.table, self.getAllFields())

    # Получить все поля объекта для его сериализации
    def getAllFields(self):
        return ()
    


    


