from server.bean.inference_task.obj_inference_task import ObjInferenceTaskFilter, ObjInferenceTask
from server.dao.inference_task.inference_task_dao import InferenceTaskDao


class InferenceTaskService:
    @staticmethod
    def find_count(task_filter: ObjInferenceTaskFilter) -> int:
        return InferenceTaskDao.find_count(task_filter)

    @staticmethod
    def find_list(task_filter: ObjInferenceTaskFilter) -> list[ObjInferenceTask]:
        return InferenceTaskDao.find_list(task_filter)