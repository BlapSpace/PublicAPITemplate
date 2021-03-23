from .. import essentials
from fastapi.responses import JSONResponse
import json
import os

#servicesStatusReport.send() |  feedback, process, timeAndDate, timeCount, feedbackLevel

### Vars ###

serviceName = os.environ()["serviceName"]

### FastAPI Init ###

app, UnicornException = essential.init(serviceName)

### Service Functions ###

@app.get("/")
async def main():
    return JSONResponse(content={"message": "Hello World"})


#raise UnicornException(errorCode="101", errorContext="I'm a Context", statusCode=500)


#Neo4J Sec / Connector - OK
#Error Handler - OK
#MongoDB Connector - OK
#Redis Connector - OK
#ElasticSearch Connector - OK
#ElasticSearch Feedback (SystemFeedback)
#SystemFeedback DBs
#dbConnector