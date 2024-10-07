from server.bean.reference_audio.obj_inference_category import ObjInferenceCategory
from server.dao.reference_audio.reference_category_dao import ReferenceCategoryDao


class ReferenceCategoryService:
    @staticmethod
    def add_category(target_category: str) -> None:
        exists = ReferenceCategoryService.exists_category_name(target_category)
        if exists > 0:
            return
        ReferenceCategoryDao.insert_category(ObjInferenceCategory(name=target_category))

    @staticmethod
    def exists_category_name(target_category: str) -> int:
        return ReferenceCategoryDao.exists_category_name(target_category)