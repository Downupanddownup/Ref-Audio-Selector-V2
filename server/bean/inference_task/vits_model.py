from server.bean.base_model import BaseModel


class VitsModel(BaseModel):
    def __init__(self, version=None, name=None, path=None):
        self.version = version
        self.name = name
        self.path = path
