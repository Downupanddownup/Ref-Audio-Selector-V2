
class Filter:
    def __init__(self, form_data):
        self.page = form_data.get('page')
        self.limit = form_data.get('limit')
        self.order_by = form_data.get('order_by')
        self.order_by_desc = form_data.get('order_by_desc')
        
    def get_order_by_sql(self) -> str:
        if self.order_by == "":
            return ""
        return f" ORDER BY {self.order_by} {self.order_by_desc}"
    def get_limit_sql(self) -> str:
        if self.page < 1 or self.limit < 1:
            return ""
        return f" LIMIT {self.limit} OFFSET {(self.page - 1)*self.limit}"