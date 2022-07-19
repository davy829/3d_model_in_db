from DBhandler.DBhandler import DBHandler
from models.BaseModel import BaseModel


class Dmodel(BaseModel):
    def __init__(self, id, name, description):
        super().__init__()
        self._id = id
        self.name = name
        self._description = description
        
    @staticmethod
    def get_table():
        return "'Models'"

    def get_id(self):
        return self._id
    
    def get_description(self):
        return self._description

    @staticmethod
    def getAll(dbhandler: DBHandler) -> list:
        return dbhandler.getItems(Dmodel.get_table())

    # Получить элемент модели по ID
    @staticmethod
    def getItemByID(id: int, dbhandler: DBHandler) -> tuple:
        return dbhandler.getItemById(Dmodel.get_table(), id)

    def getAllFields(self):
        return (self._id, self.name, self._description)
    
    def updateDescItem(self, dbhandler: DBHandler) -> bool:
        return dbhandler.updateItemById(type(self).get_table(), self._description, self._id)