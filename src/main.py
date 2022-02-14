import configurations
import time
import uuid
import uvicorn

from about_response import BizException, CodeAndMessage, Result
from endpoint import health_endpoint
from fastapi import FastAPI, Request
from logger_factory import logger
from starlette.responses import JSONResponse

app = FastAPI(title='Rest API Doc', version='1.0', description='')


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    """
    Global Exception Handler.
    发生异常时, 不会记录 access log.
    """

    logger.error('[] Global Exception Handler >>>')
    logger.exception(exc)
    logger.error('[] <<< Global Exception Handler')
    if isinstance(exc, BizException):
        return JSONResponse(status_code=200, content=Result.err(exc.code, exc.message))
    else:
        return JSONResponse(status_code=200, content=Result.err(CodeAndMessage.server_error_code, exc.__str__()))


@app.middleware('http')
async def log_and_add_request_id(request: Request, call_next):
    occurred_at = time.time()

    request_id = str(uuid.uuid4()).replace('-', '').upper()
    request.state.profile = {'request_id': request_id}

    response = await call_next(request)
    response.headers['X-Request-Id'] = request_id

    micro_duration = int(round((time.time() - occurred_at) * 1000000))
    logger.info('[] Access occurred_at: {}, request_id: {}, method: {}, uri: {}, duration: {}', occurred_at, request_id, request.method, request.url.path, micro_duration)

    return response


health_endpoint.setup(app)

logger.info('[] start >')

uvicorn.run(app, host="0.0.0.0", port=configurations.server_port)
