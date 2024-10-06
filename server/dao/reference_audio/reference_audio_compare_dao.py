from server.bean.reference_audio.obj_reference_audio_compare_detail import ObjReferenceAudioCompareDetail
from server.bean.reference_audio.obj_reference_audio_compare_task import ObjReferenceAudioCompareTask
from server.dao.data_base_manager import SQLExecutor


class ReferenceAudioCompareDao:
    @staticmethod
    def insert_task(task: ObjReferenceAudioCompareTask) -> int:
        sql = '''
            INSERT INTO tab_obj_reference_audio_compare_task(AudioId,CategoryName,Status,Remark,CreateTime) VALUES (?,?,?,?,datetime('now'))
            '''
        return SQLExecutor.insert(sql, (
            task.audio_id,
            task.category_name,
            task.status,
            task.remark
        ))

    @staticmethod
    def get_task_by_id(task_id: int) -> ObjReferenceAudioCompareTask:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT * FROM tab_obj_reference_audio_compare_task where id = ? LIMIT 1
            '''

        records = SQLExecutor.execute_query(select_sql, (task_id,))

        list = []

        for data in records:
            list.append(ObjReferenceAudioCompareTask(
                id=data.get('Id'),
                audio_id=data.get('AudioId'),
                category_name=data.get('CategoryName'),
                status=data.get('Status'),
                remark=data.get('Remark'),
                create_time=data.get('CreateTime')
            ))
        if len(list) == 0:
            return None
        return list[0]

    @staticmethod
    def update_task_status(task_id: int, status: int) -> int:
        sql = '''
            UPDATE tab_obj_reference_audio_compare_task SET Status = ? WHERE Id = ?
            '''
        return SQLExecutor.execute_update(sql, (
            task_id,
            status
        ))

    @staticmethod
    def batch_insert_task_detail(detail_list: list[ObjReferenceAudioCompareDetail]) -> int:
        sql = '''
            INSERT INTO tab_obj_reference_audio_compare_detail(TaskId,CompareAudioId,Score,CreateTime) VALUES (?,?,?,datetime('now'))
            '''
        return SQLExecutor.batch_execute(sql, [(
            x.task_id,
            x.compare_audio_id,
            x.score
        ) for x in detail_list])

