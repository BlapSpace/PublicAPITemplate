import json, os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from connectors import elasticsearchConnector, mongoDBConnector, redisConnector

def send(feedback, process, timeAndDate, timeCount, statusLevel):
    ### ElasticSearch ###
    for tryNum in range(1, 4):
        statusResponse = elasticsearchConnector.connect().index(index=os.environ()["servicesStatusReport"], body={"tryNum": tryNum, "tryType": "ElasticSearch", "service": os.environ()[
            "serviceName"], "timeAndDate": timeAndDate, "timeCount": timeCount, "statusLevel": statusLevel, "process": process, "feedback": feedback})["result"]
        if statusResponse == "created":
            return None
    print('[ERROR][servicesStatusReport]: ElasticSearch "index" error')
    ### MongoDB ###
    for tryNum in range(1, 4):
        try:
            mongoDBConnector.connect()["servicesStatusReportFallback"].insert_one(
                {"tryNum": tryNum, "tryType": "MongoDB", "service": os.environ()[
                    "serviceName"], "timeAndDate": timeAndDate, "timeCount": timeCount, "statusLevel": statusLevel, "process": process, "feedback": feedback})
            return None
        except Exception as e:
            pass
    print('[ERROR][servicesStatusReport]: MongoDB "insert_one" error')
    print(e)
    ### Redis ###
    for tryNum in range(1, 4):
        try:
            redisConnector.connect(15).lpush("servicesStatusReportFallback", json.dumps(
                {"tryNum": tryNum, "tryType": "Redis", "service": os.environ()[
                    "serviceName"], "timeAndDate": timeAndDate, "timeCount": timeCount, "statusLevel": statusLevel, "process": process, "feedback": feedback}))
            return None
        except Exception as e:
            pass
    print('[ERROR][servicesStatusReport]: Redis "lpush" error')
    print(e)
    print("[ERROR][servicesStatusReport]: All DataStores for servicesStatusReport(Fallback) are broken")
    # exit()

# Retryss?
