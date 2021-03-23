import servicesStatusReport
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os
import time
import datetime

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
        timeAndDate = datetime.datetime()
        timeCount = time.time()

        ### Base init ###
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
        servicesStatusReport.send(None, "GroundInit", timeAndDate, timeCount, 0)
        return app, UnicornException
    except Exception as e:
        servicesStatusReport.send(e, "GroundInit", timeAndDate, timeCount, 4)
