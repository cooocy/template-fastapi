from about_response import BizException, CodeAndMessage, Result
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

    @app.get('/health/biz-error', summary='Raise BizException.')
    def health_error(m: Optional[str] = ''):
        """
        `m`: **optional**, string \n
        """
        raise BizException(CodeAndMessage.server_error_code, 'Biz Exception: ' + m)

    @app.get('/health/error', summary='Raise Exception.')
    def health_error(m: Optional[str] = ''):
        """
        `m`: **optional**, string \n
        """
        raise Exception('Exception: ' + m)
