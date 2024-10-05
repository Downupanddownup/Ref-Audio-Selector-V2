from server.bean.base_model import BaseModel


class ObjReferenceAudio(BaseModel):
    def __init__(self, id=None, audio_name=None, audio_path=None, content=None,
                 language=None, category=None, audio_length=None, create_time=None):
        self.id = id  # 主键ID，允许从外部传入
        self.audio_name = audio_name  # 音频名称
        self.audio_path = audio_path  # 音频路径
        self.content = content  # 音频内容
        self.language = language  # 音频语种
        self.category = category  # 音频分类
        self.audio_length = audio_length  # 音频时长
        self.create_time = create_time  # 创建时间，默认为当前时间

    @classmethod
    def from_dict_sql(cls, data):
        # 使用提供的字典初始化类的实例
        return cls(
            id=data.get('Id'),
            audio_name=data.get('AudioName'),
            audio_path=data.get('AudioPath'),
            content=data.get('Content'),
            language=data.get('Language'),
            category=data.get('Category'),
            audio_length=data.get('AudioLength'),
            create_time=data.get('CreateTime')
        )

    def __str__(self):
        return (f"Id: {self.id}, AudioName: {self.audio_name}, "
                f"AudioPath: {self.audio_path}, Content: {self.content}, "
                f"Language: {self.language}, Category: {self.category}, "
                f"AudioLength: {self.audio_length}, CreateTime: {self.create_time}")