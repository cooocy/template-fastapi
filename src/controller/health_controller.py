from about_response import Result, BizException, CodeAndMessage
from typing import Optional


def setup(app):
    @app.get('/health/check', summary='Health check.')
    def health_check():
        return Result.ok('Hello!')

    @app.get('/health/error', summary='Throw error.')
    def health_error(m: Optional[str] = ''):
        """
        `m`: **optional**, string \n
        """

        if m == '':
            raise BizException(CodeAndMessage.args_error_code, '[m] can not be blank!')
        else:
            raise BizException(CodeAndMessage.args_error_code, m)
