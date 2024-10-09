from server.bean.inference_task.obj_inference_task import ObjInferenceTaskFilter, ObjInferenceTask
from server.dao.data_base_manager import DBSlaveSQLExecutor


class InferenceTaskDao:
    @staticmethod
    def find_count(task_filter: ObjInferenceTaskFilter) -> int:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT COUNT(1) FROM tab_obj_inference_task where 1=1
            '''

        condition_sql, condition = task_filter.make_sql()

        select_sql += condition_sql

        count = DBSlaveSQLExecutor.get_count(select_sql, condition)

        return count

    @staticmethod
    def find_list(task_filter: ObjInferenceTaskFilter) -> list[ObjInferenceTask]:
        # 查询所有记录的SQL语句
        select_sql = '''
            SELECT * FROM tab_obj_inference_task where 1=1
            '''

        condition_sql, condition = task_filter.make_sql()

        select_sql += condition_sql

        select_sql += task_filter.get_order_by_sql()

        select_sql += task_filter.get_limit_sql()

        records = DBSlaveSQLExecutor.execute_query(select_sql, condition)

        text_list = []

        for data in records:
            text_list.append(ObjInferenceTask(
                id=data.get('Id'),
                task_name=data.get('TaskName'),
                compare_type=data.get('CompareType'),
                gpt_sovits_version=data.get('GptSovitsVersion'),
                gpt_model_name=data.get('GptModelName'),
                vits_model_name=data.get('VitsModelName'),
                top_k=data.get('TopK'),
                top_p=data.get('TopP'),
                temperature=data.get('Temperature'),
                text_delimiter=data.get('TextDelimiter'),
                speed=data.get('Speed'),
                other_parameters=data.get('OtherParameters'),
                inference_status=data.get('InferenceStatus'),
                execute_text_similarity=data.get('ExecuteTextSimilarity'),
                execute_audio_similarity=data.get('ExecuteAudioSimilarity'),
                create_time=data.get('CreateTime')
            ))
        return text_list
