from server.bean.inference_task.obj_inference_task import ObjInferenceTaskFilter, ObjInferenceTask
from server.bean.inference_task.obj_inference_task_audio import ObjInferenceTaskAudio
from server.bean.inference_task.obj_inference_task_compare_params import ObjInferenceTaskCompareParams
from server.bean.inference_task.obj_inference_task_text import ObjInferenceTaskText
from server.bean.reference_audio.obj_reference_audio import ObjReferenceAudioFilter
from server.common.custom_exception import CustomException
from server.dao.inference_task.inference_task_dao import InferenceTaskDao
from server.service.reference_audio.reference_audio_service import ReferenceAudioService
from server.util.util import ValidationUtils


class InferenceTaskService:
    @staticmethod
    def find_count(task_filter: ObjInferenceTaskFilter) -> int:
        return InferenceTaskDao.find_count(task_filter)

    @staticmethod
    def find_list(task_filter: ObjInferenceTaskFilter) -> list[ObjInferenceTask]:
        return InferenceTaskDao.find_list(task_filter)

    @staticmethod
    def add_inference_task(task: ObjInferenceTask) -> int:
        InferenceTaskService.check_inference_task(task)
        if task.compare_type == 'refer_audio':
            reference_audio_list = ReferenceAudioService.find_list(ObjReferenceAudioFilter({
                'category_list_str': ','.join(f'"{p.audio_category}"' for p in task.param_list)
            }))
            task.audio_list = [ObjInferenceTaskAudio(
                audio_id=audio.id,
                audio_name=audio.audio_name,
                audio_path=audio.audio_path,
                audio_content=audio.content,
                audio_language=audio.language
            ) for audio in reference_audio_list]

        task_id = InferenceTaskDao.insert_inference_task(task)
        if task_id < 1:
            raise CustomException("添加推理任务失败")
        for param in task.param_list:
            param.task_id = task_id
        InferenceTaskDao.batch_insert_task_param(task.param_list)
        for audio in task.audio_list:
            audio.task_id = task_id
        InferenceTaskDao.batch_insert_task_audio(task.audio_list)
        for text in task.text_list:
            text.task_id = task_id
        InferenceTaskDao.batch_insert_task_text(task.text_list)
        return task_id

    @staticmethod
    def check_inference_task(task: ObjInferenceTask) -> None:
        if ValidationUtils.is_empty(task.task_name):
            raise CustomException("任务名不能为空")
        if ValidationUtils.is_empty(task.compare_type):
            raise CustomException("比较类型不能为空")
        if len(task.param_list) == 0:
            raise CustomException("对比参数不能为空")
        if len(task.text_list) == 0:
            raise CustomException("推理文本不能为空")
        if task.compare_type != 'refer_audio' and len(task.audio_list) == 0:
            raise CustomException("音频列表不能为空")

    @staticmethod
    def find_whole_inference_task_by_id(task_id: int) -> ObjInferenceTask:
        task_list = InferenceTaskService.find_list(ObjInferenceTaskFilter({'id': task_id}))
        if len(task_list) == 0:
            return None
        task = task_list[0]
        task.param_list = InferenceTaskService.get_task_param_list_by_task_id(task_id)
        task.audio_list = InferenceTaskService.get_task_audio_list_by_task_id(task_id)
        task.text_list = InferenceTaskService.get_task_text_list_by_task_id(task_id)
        return task

    @staticmethod
    def get_task_param_list_by_task_id(task_id: int) -> list[ObjInferenceTaskCompareParams]:
        return InferenceTaskDao.get_task_param_list_by_task_id(task_id)

    @staticmethod
    def get_task_audio_list_by_task_id(task_id: int) -> list[ObjInferenceTaskAudio]:
        return InferenceTaskDao.get_task_audio_list_by_task_id(task_id)

    @staticmethod
    def get_task_text_list_by_task_id(task_id: int) -> list[ObjInferenceTaskText]:
        return InferenceTaskDao.get_task_text_list_by_task_id(task_id)

    @staticmethod
    def save_inference_task(task: ObjInferenceTask) -> int:
        if task.id < 1:
            raise CustomException("任务id不能为空")
        InferenceTaskService.check_inference_task(task)
        if task.compare_type == 'refer_audio':
            reference_audio_list = ReferenceAudioService.find_list(ObjReferenceAudioFilter({
                'category_list_str': ','.join(f'"{p.audio_category}"' for p in task.param_list)
            }))
            task.audio_list = [ObjInferenceTaskAudio(
                audio_id=audio.id,
                audio_name=audio.audio_name,
                audio_path=audio.audio_path,
                audio_content=audio.content,
                audio_language=audio.language
            ) for audio in reference_audio_list]

        task_id = task.id

        result = InferenceTaskDao.update_inference_task(task)
        if result < 1:
            raise CustomException("修改推理任务失败")

        InferenceTaskDao.delete_task_param_by_task_id(task_id)
        InferenceTaskDao.delete_task_audio_by_task_id(task_id)
        InferenceTaskDao.delete_task_text_by_task_id(task_id)

        for param in task.param_list:
            param.task_id = task_id
        InferenceTaskDao.batch_insert_task_param(task.param_list)
        for audio in task.audio_list:
            audio.task_id = task_id
        InferenceTaskDao.batch_insert_task_audio(task.audio_list)
        for text in task.text_list:
            text.task_id = task_id
        InferenceTaskDao.batch_insert_task_text(task.text_list)
        return result
