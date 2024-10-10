from server.bean.result_evaluation.obj_inference_task_result_audio import ObjInferenceTaskResultAudio
from server.dao.result_evaluation.result_evaluation_dao import ResultEvaluationDao
from server.service.inference_task.inference_task_service import InferenceTaskService


class ResultEvaluationService:
    @staticmethod
    def find_task_result_audio_list_by_task_id(task_id: int) -> list[ObjInferenceTaskResultAudio]:
        task = InferenceTaskService.find_whole_inference_task_by_id(task_id)
        result_audio_list = ResultEvaluationDao.find_task_result_audio_list_by_task_id(task_id)
        if task and result_audio_list:
            param_list = task.param_list
            audio_list = task.audio_list
            text_list = task.text_list
            for result_audio in result_audio_list:
                for param in param_list:
                    if result_audio.compare_param_id == param.id:
                        result_audio.obj_param = param
                        break
                for audio in audio_list:
                    if result_audio.audio_id == audio.id:
                        result_audio.obj_audio = audio
                        break
                for text in text_list:
                    if result_audio.text_id == text.id:
                        result_audio.obj_text = text
                        break
                result_audio.obj_task = task
            task.param_list = []
            task.audio_list = []
            task.text_list = []
            return result_audio_list
        return []

    @staticmethod
    def batch_insert_task_result_audio(result_audio_list: list[ObjInferenceTaskResultAudio]):
        return ResultEvaluationDao.batch_insert_task_result_audio(result_audio_list)

    @staticmethod
    def batch_update_task_result_audio_status_file_length(task_result_audio_list: list[ObjInferenceTaskResultAudio]):
        return ResultEvaluationDao.batch_update_task_result_audio_status_file_length(task_result_audio_list)
