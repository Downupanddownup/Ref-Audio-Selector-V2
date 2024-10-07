from server.bean.reference_audio.obj_inference_category import ObjInferenceCategory
from server.dao.data_base_manager import SQLExecutor


class ReferenceCategoryDao:
    @staticmethod
    def exists_category_name(category: str) -> int:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT COUNT(1) FROM tab_obj_inference_category where Name = ? 
            '''

        count = SQLExecutor.get_count(select_sql, (category,))

        return count

    @staticmethod
    def insert_category(category: ObjInferenceCategory) -> int:
        sql = '''
            INSERT INTO tab_obj_inference_category(Name,CreateTime) VALUES (?,datetime('now'))
            '''
        return SQLExecutor.insert(sql, (
            category.name,
        ))