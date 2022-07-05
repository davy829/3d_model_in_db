from models.BaseModel import BaseModel


class Dmodel(BaseModel):
    def __init__(self, id, link, description):
        super().__init__()
        self._id = id
        self._link = link
        self._description = description

    table = "Models"

    def getAllFields(self):
        return (self._id, self._link, self._description)