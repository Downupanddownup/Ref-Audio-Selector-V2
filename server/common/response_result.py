from server.bean.base_model import BaseModel


def convert_list_to_camel_case_dicts(list):

    result = []
    for item in list:
        if isinstance(item, BaseModel) and hasattr(item, 'to_camel_case_dict'):
            result.append(item.to_camel_case_dict())
        else:
            result.append(item)
    return result


class ResponseResult:
    def __init__(self, code=0, msg="success", count=0, data=None):
        self.code = code
        self.msg = msg
        self.count = count
        self.data = convert_list_to_camel_case_dicts(data if data is not None else [])

    def __str__(self):
        return f"ResponseResult(code={self.code}, msg='{self.msg}', count={self.count}, data={self.data})"
