from typing import Dict

from server.bean.reference_audio.obj_reference_audio import ObjReferenceAudio
from server.dao.data_base_manager import DatabaseConnection, SQLExecutor


class ReferenceAudioDao:
    @staticmethod
    def search() -> list[ObjReferenceAudio]:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT * FROM tab_obj_reference_audio where id = ? ;
            '''

        records = SQLExecutor.execute_query(select_sql, (1,))

        list = []

        for record in records:
            list.append(ObjReferenceAudio.from_dict_sql(record))
        return list
