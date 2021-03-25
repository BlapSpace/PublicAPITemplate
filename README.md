# PublicAPITemplate
The template for all public APIs

--------------------------

**API Ground Structure**
  - **essentials**
    - errorHandler.json
    - essential.py
      - init()
    - servicesStatusReport.py
      - send()
  - **connectors**
    - elasticsearchConnector.py
      - connect()
    - mongodbConnector.py
      - connect()
    - redisConnector.py
      - connect()
    - neo4jConnector.py
      - connect()
  - **app**
    - main.py
    - ...

--------------------------

# GUIDE

### Error Handler

`raise UnicornException(internalErrorCode="101", errorContext="I'm a Context", statusCode=500)`
---
- errorCode => The internal error code for the errorHandler and other system APIs 
- errorContext => The request from user and maby other data
- statusCode => HTTP error code like 404 or 500

### Service Status Report

`servicesStatusReport.send(serviceName, databases, errorCode, feedback, process, timeAndDate, timeCount, feedbackLevel)`
---
- serviceName => The name from the service
- databases => A list with elasticsearch-, mongodb-, redis-Client
- internalErrorCode => This is the internal error code for other APIs or to find faster error collections
- feedback => The errir or other. If only normal status report than make None as feedback
- process => What a function or process
- timeAndDate => Time and Date
- timeCount => How much time needed the process
- feedbackLevel => How critical is the report? 0=Normal, ..., 4=Down
