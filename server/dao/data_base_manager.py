import os.path
import sqlite3
from typing import List, Dict

from server.dao.init_db import init_table


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.workspace = 'workspace'
        self.role_name = ''
        self.db_path = ''

    def update_db_path(self, role_name: str):
        self.role_name = role_name
        self.db_path = f'{self.get_work_dir()}\\ref_audio_selector.db'
        init_table(self.db_path)
    
    def get_work_dir(self) -> str:
        work_dir = f'{self.workspace}\\{self.role_name}'
        if not os.path.exists(work_dir):
            os.makedirs(work_dir)
        return work_dir


# 读取配置文件
db_config = DatabaseConfig()


class DatabaseConnection:
    def __init__(self):
        self.db_path = db_config.db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()


class SQLExecutor:
    def __init__(self):
        pass

    @staticmethod
    def execute_query(query: str, parameters: tuple = ()) -> List[Dict]:
        """
        执行 SQL 查询并返回查询结果和列名。

        :param query: SQL 查询语句。
        :param parameters: SQL 查询参数（可选）。
        :return: 查询结果列表，每个元素是一个包含列名和值的字典。
        """
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, parameters)

            # 获取列名
            column_names = [description[0] for description in cursor.description]

            # 获取所有记录
            records = cursor.fetchall()

            # 将记录转换为字典形式
            results = [dict(zip(column_names, record)) for record in records]

            return results
        pass

    @staticmethod
    def get_count(query: str, parameters: tuple = ()) -> int:
        """
        执行 SQL 查询并返回查询结果和列名。

        :param query: SQL 查询语句。
        :param parameters: SQL 查询参数（可选）。
        :return: 查询结果列表，每个元素是一个包含列名和值的字典。
        """
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, parameters)

            # 获取数量
            return cursor.fetchone()[0]

    @staticmethod
    def execute_update(query: str, parameters: tuple = ()) -> int:
        """
        执行 SQL 更新（如插入、更新或删除）。

        :param query: SQL 更新语句。
        :param parameters: SQL 更新语句的参数（可选）。
        :return: 影响的行数。
        """
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            rows_affected = cursor.execute(query, parameters).rowcount
            # 提交事务
            connection.commit()
            return rows_affected

    @staticmethod
    def insert(query: str, parameters: tuple = ()) -> int:
        """
        执行 SQL 更新（如插入、更新或删除）。

        :param query: SQL 更新语句。
        :param parameters: SQL 更新语句的参数（可选）。
        :return: 影响的行数。
        """
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            inserted_id = cursor.execute(query, parameters).lastrowid
            # 提交事务
            connection.commit()
            return inserted_id


    @staticmethod
    def batch_execute(query: str, parameters_list: List[tuple]) -> int:
        """
        执行批量插入操作。

        :param query: SQL 插入语句。
        :param parameters_list: SQL 插入语句的参数列表。
        :return: 影响的行数。
        """
        affected_rows = 0
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            # 显式开始事务
            cursor.execute('BEGIN')
            try:
                # 批量插入数据
                cursor.executemany(query, parameters_list)
                affected_rows = cursor.rowcount
                # 提交事务
                connection.commit()
            except Exception as e:
                # 如果发生异常，则回滚事务
                connection.rollback()
                raise e
            return affected_rows
        