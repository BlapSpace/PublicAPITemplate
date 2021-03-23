from fastapi.responses import JSONResponse
import json, os, sys, inspect, time, datetime
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from essentials import essential

#servicesStatusReport.send() |  databases, feedback, process, timeAndDate, timeCount, feedbackLevel

### Vars ###

#serviceName = os.environ()["serviceName"]

### FastAPI and Databases Init ###

app, UnicornException, esClient, mongoDBClient, redisClient = essential.init()
databases = [esClient, mongoDBConnector, redisClient]

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