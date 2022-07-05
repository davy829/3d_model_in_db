from models.BaseModel import BaseModel


class Dmodel(BaseModel):
    def __init__(self, id, description):
        super().__init__()
        self._id = id
        self._description = description

    table = "Models"

    def get_id(self):
        return self._id

    def getAllFields(self):
        return (self._id, self._description)