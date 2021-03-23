from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json, os, sys, inspect, time, datetime
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from essentials import servicesStatusReport

### Exception Handling Class ###


class UnicornException(Exception):
    def __init__(self, errorCode: str, errorContext: str, statusCode: str):
        self.errorCode = errorCode
        self.errorContext = errorContext
        self.statusCode = statusCode

### Init essentials ###


def init():
    try:
        ### Get Values for Status Report ###
        timeAndDate = datetime.datetime.now()
        timeCount = time.time()

        ### Base init ##timeAndDate#
        app = FastAPI()

        ### Error Handler load ###
        with open("errorHandler.json", "r") as file:
            errorHandler = json.load(
                file)["services"][os.environ()["serviceName"]]

        ### CORS ###
        origins = ["*"]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])

        ### Exception Handling Function ###
        @app.exception_handler(UnicornException)
        async def unicorn_exception_handler(request: Request, exc: UnicornException):
            return JSONResponse(
                status_code=exc.statusCode,
                content={"errorContext": exc.errorContext,
                         "message": errorHandler[exc.errorCode]})

        ### Send Services Status Report ###
        servicesStatusReport.send(None, "GroundInit", timeAndDate, time.time() - timeCount, 0)
        return app, UnicornException
    except Exception as e:
        servicesStatusReport.send(e, "GroundInit", timeAndDate, time.time() - timeCount, 4)
