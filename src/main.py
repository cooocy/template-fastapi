import configurations
import logger_factory
import time
import uuid
import uvicorn

from about_response import BizException, Result
from controller import health_controller
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI(title='Rest API Doc', version='1.0', description='')


@app.exception_handler(BizException)
async def unicorn_exception_handler(request: Request, exc: BizException):
    return JSONResponse(status_code=200, content=Result.err(exc.code, exc.message))


@app.middleware('http')
async def log_and_add_request_id(request: Request, call_next):
    begin_time = time.time()

    request_id = str(uuid.uuid4()).upper()
    response = await call_next(request)
    response.headers['X-Request-Id'] = request_id

    micro_duration = int(round((time.time() - begin_time) * 1000000))

    logger_factory.logger.info('[] access. request-id: {}, path: {}, duration: {}', request_id, request.url.path,
                               micro_duration)
    return response


health_controller.setup(app)

logger_factory.logger.info('[] start >')

uvicorn.run(app, host="0.0.0.0", port=configurations.server_port)
