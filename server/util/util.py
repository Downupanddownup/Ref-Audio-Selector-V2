class ValidationUtils:
    @staticmethod
    def is_empty(value):
        if value is None:
            return True
        if isinstance(value, str) and not value.strip():
            return True
        if isinstance(value, (list, tuple, set, dict)) and not value:
            return True
        return False
