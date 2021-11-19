from about_response import Result, BizException, CodeAndMessage
from fastapi import Request
from logger_factory import logger
from typing import Optional


def setup(app):
    """
    Set up.
    """

    @app.get('/health/check', summary='Health check.')
    def health_check(request: Request):
        """
        Health check.
        """

        logger.info('[] health check. request_id: {}', request.state.profile['request_id'])
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
