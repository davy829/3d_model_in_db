from DBhandler.DBhandler import DBHandler
from models.BaseModel import BaseModel


class Dmodel(BaseModel):
    def __init__(self, id, description):
        super().__init__()
        self._id = id
        self._description = description

    @staticmethod
    def get_table():
        return "'3Dmodels'"

    def get_id(self):
        return self._id
    
    def get_description(self):
        return self._description

    @staticmethod
    def getAll(dbhandler: DBHandler) -> list:
        return dbhandler.getItems(Dmodel.get_table())

    def getAllFields(self):
        return (self._id, self._description)