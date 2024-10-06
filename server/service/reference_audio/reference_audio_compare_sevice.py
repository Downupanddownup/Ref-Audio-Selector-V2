from server.bean.reference_audio.obj_reference_audio_compare_detail import ObjReferenceAudioCompareDetail
from server.bean.reference_audio.obj_reference_audio_compare_task import ObjReferenceAudioCompareTask
from server.dao.reference_audio.reference_audio_compare_dao import ReferenceAudioCompareDao


class ReferenceAudioCompareService:
    @staticmethod
    def insert_task(task: ObjReferenceAudioCompareTask) -> int:
        return ReferenceAudioCompareDao.insert_task(task)

    @staticmethod
    def get_task_by_id(task_id: int) -> ObjReferenceAudioCompareTask:
        return ReferenceAudioCompareDao.get_task_by_id(task_id)

    @staticmethod
    def update_task_to_fail(task_id: int) -> int:
        return ReferenceAudioCompareDao.update_task_status(task_id, 3)

    @staticmethod
    def update_task_to_start(task_id: int) -> int:
        return ReferenceAudioCompareDao.update_task_status(task_id, 1)

    @staticmethod
    def update_task_to_finish(task_id: int) -> int:
        return ReferenceAudioCompareDao.update_task_status(task_id, 2)

    @staticmethod
    def batch_insert_task_detail(detail_list: list[ObjReferenceAudioCompareDetail]) -> int:
        return ReferenceAudioCompareDao.batch_insert_task_detail(detail_list)