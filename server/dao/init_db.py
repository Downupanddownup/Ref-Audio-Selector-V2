import sqlite3


def init_table(db_path):
    # 连接到SQLite数据库，如果不存在则创建
    conn = sqlite3.connect(db_path)

    # 创建一个游标对象用于执行SQL命令
    cursor = conn.cursor()

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_reference_audio (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        AudioName TEXT COMMENT '音频名称', -- SQLite不支持直接在列定义中添加注释
        AudioPath TEXT COMMENT '音频路径',
        Content TEXT COMMENT '音频内容',
        Language TEXT COMMENT '音频语种',
        Category TEXT COMMENT '音频分类',
        AudioLength INTEGER COMMENT '音频时长',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_inference_task (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        CompareType TEXT COMMENT '比较类型', -- SQLite不支持直接在列定义中添加注释
        GptSovitsVersion TEXT COMMENT '模型版本',
        GptModelName TEXT COMMENT 'GPT模型名称',
        VitsModelName TEXT COMMENT 'Vits模型名称',
        TopK REAL COMMENT 'top_k值', -- MySQL中的float类型在SQLite中对应REAL类型
        TopP REAL COMMENT 'top_p值',
        Temperature REAL COMMENT '温度',
        TextDelimiter TEXT COMMENT '文本分隔符',
        Speed REAL COMMENT '语速',
        OtherParameters TEXT COMMENT '其余参数',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_inference_task_text (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        TaskId INTEGER COMMENT '推理任务id', -- SQLite不支持直接在列定义中添加注释
        TextId INTEGER COMMENT '推理文本id',
        TextContent TEXT COMMENT '推理文本', -- MySQL中的text类型在SQLite中对应TEXT类型
        TextLanguage TEXT COMMENT '文本语种',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_inference_task_audio (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        TaskId INTEGER COMMENT '推理任务id', -- SQLite不支持直接在列定义中添加注释
        AudioId INTEGER COMMENT '音频id',
        AudioName TEXT COMMENT '音频名称', -- 使用TEXT类型，虽然也可以使用VARCHAR
        AudioPath TEXT COMMENT '音频路径',
        AudioContent TEXT COMMENT '音频内容',
        AudioLanguage TEXT COMMENT '音频语种',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_inference_task_compare_params (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        TaskId INTEGER COMMENT '任务id', -- SQLite不支持直接在列定义中添加注释
        GptSovitsVersion TEXT COMMENT '模型版本',
        GptModelName TEXT COMMENT 'GPT模型名称',
        VitsModelName TEXT COMMENT 'Vits模型名称',
        TopK REAL COMMENT 'top_k值', -- MySQL中的float类型在SQLite中对应REAL类型
        TopP REAL COMMENT 'top_p值',
        Temperature REAL COMMENT '温度',
        TextDelimiter TEXT COMMENT '文本分隔符',
        Speed REAL COMMENT '语速',
        OtherParameters TEXT COMMENT '其余参数',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 创建一个新表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tab_obj_inference_task_result_audio (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite使用AUTOINCREMENT关键字实现自动增长
        TaskId INTEGER COMMENT '推理任务id', -- SQLite不支持直接在列定义中添加注释
        TextId INTEGER COMMENT '推理文本id',
        AudioId INTEGER COMMENT '参考音频id',
        CompareParamId INTEGER COMMENT '比对参数id',
        Path TEXT COMMENT '音频地址',
        AudioLength REAL COMMENT '时长',
        AsrText TEXT COMMENT 'asr文本',
        AsrSimilarScore REAL COMMENT '文本相似度',
        AudioSimilarScore REAL COMMENT '音频相似度',
        Score SMALLINT COMMENT '评分',
        LongTextScore SMALLINT COMMENT '长文评分',
        Remark TEXT COMMENT '备注',
        CreateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- SQLite中默认值可以直接设置
    );
    ''')

    # 提交事务（如果没有这一步，则不会保存更改）
    conn.commit()

    # 关闭连接
    conn.close()
