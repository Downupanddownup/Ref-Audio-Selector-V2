from server.bean.inference_task.gpt_model import GptModel
from server.bean.inference_task.vits_model import VitsModel


class ModelManagerService:
    @staticmethod
    def get_gpt_model_list() -> list[GptModel]:
        pass

    @staticmethod
    def get_vits_model_list() -> list[VitsModel]:
        pass

    @staticmethod
    def get_vits_model_by_name(gpt_sovits_version, vits_model_name):
        return next(filter(lambda model: model.equals(gpt_sovits_version, vits_model_name),
                           ModelManagerService.get_vits_model_list()))

    @staticmethod
    def get_gpt_model_by_name(gpt_sovits_version, gpt_model_name):
        return next(filter(lambda model: model.equals(gpt_sovits_version, gpt_model_name),
                           ModelManagerService.get_gpt_model_list()))
