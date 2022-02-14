class Result:
    @staticmethod
    def ok(data=None):
        return {'success': True, 'code': 0, 'message': None, 'data': data}

    @staticmethod
    def err(code: int, message: str):
        return {'success': False, 'code': code, 'message': message, 'data': None}


class BizException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class CodeAndMessage:
    args_error_code = 1
    args_error_msg = 'args error'

    server_error_code = 100
