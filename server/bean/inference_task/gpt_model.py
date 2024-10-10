from server.bean.base_model import BaseModel


class GptModel(BaseModel):
    def __init__(self, version=None, name=None, path=None):
        self.version = version
        self.name = name
        self.path = path

    def equals(self, version, name):
        return self.version == version and self.name == name
