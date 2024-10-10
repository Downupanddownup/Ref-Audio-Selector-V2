from server.bean.result_evaluation.obj_inference_task_result_audio import ObjInferenceTaskResultAudio
from server.dao.data_base_manager import DBSlaveSQLExecutor


class ResultEvaluationDao:
    @staticmethod
    def find_task_result_audio_list_by_task_id(task_id: int) -> list[ObjInferenceTaskResultAudio]:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT * FROM tab_obj_inference_task_result_audio where TaskId = ?
            '''

        records = DBSlaveSQLExecutor.execute_query(select_sql, (task_id,))
        record_list = []
        for data in records:
            record_list.append(ObjInferenceTaskResultAudio(
                id=data.get('Id'),
                task_id=data.get('TaskId'),
                text_id=data.get('TextId'),
                audio_id=data.get('AudioId'),
                compare_param_id=data.get('CompareParamId'),
                path=data.get('Path'),
                audio_length=data.get('AudioLength'),
                status=data.get('Status'),
                asr_text=data.get('AsrText'),
                asr_similar_score=data.get('AsrSimilarScore'),
                audio_similar_score=data.get('AudioSimilarScore'),
                score=data.get('Score'),
                long_text_score=data.get('LongTextScore'),
                remark=data.get('Remark'),
                create_time=data.get('CreateTime')
            ))
        return record_list

    @staticmethod
    def batch_insert_task_result_audio(result_audio_list: list[ObjInferenceTaskResultAudio]):
        sql = '''
        INSERT INTO tab_obj_inference_task_result_audio(TaskId,TextId,AudioId,CompareParamId,Path,AudioLength,Status,AsrText,AsrSimilarScore,AudioSimilarScore,Score,LongTextScore,Remark,CreateTime) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now'))
        '''
        return DBSlaveSQLExecutor.batch_execute(sql, [(
            x.task_id,
            x.text_id,
            x.audio_id,
            x.compare_param_id,
            x.path,
            x.audio_length,
            x.status,
            x.asr_text,
            x.asr_similar_score,
            x.audio_similar_score,
            x.score,
            x.long_text_score,
            x.remark
        ) for x in result_audio_list])

    @staticmethod
    def batch_update_task_result_audio_status_file_length(task_result_audio_list: list[ObjInferenceTaskResultAudio]):
        sql = '''
            UPDATE tab_obj_inference_task_result_audio SET 
            Status=?,
            Path=?,
            AudioLength=?
             WHERE Id = ? 
            '''
        return DBSlaveSQLExecutor.batch_execute(sql, [(
            x.status,
            x.path,
            x.audio_length,
            x.id
        ) for x in task_result_audio_list])
