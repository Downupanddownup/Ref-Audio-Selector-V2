from server.bean.base_model import BaseModel


class GptModel(BaseModel):
    def __init__(self, version=None, name=None):
        self.version = version
        self.name = name
