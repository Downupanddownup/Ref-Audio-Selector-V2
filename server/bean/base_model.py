class BaseModel:
    @staticmethod
    def snake_to_camel(snake_str):
        """Converts a snake_case string to camelCase."""
        components = snake_str.split('_')
        # 如果字符串只有一个部分，则保持不变；否则首字母大写并拼接
        return components[0] + ''.join(x.title() for x in components[1:])

    def to_camel_case_dict(self):
        """Converts the instance attributes to a dictionary with camelCase keys."""
        return {self.snake_to_camel(k): v for k, v in vars(self).items()}