from server.bean.inference_task.gpt_model import GptModel
from server.bean.inference_task.vits_model import VitsModel


class ModelManagerService:
    @staticmethod
    def get_gpt_model_list() -> list[GptModel]:
        pass

    @staticmethod
    def get_vits_model_list() -> list[VitsModel]:
        pass