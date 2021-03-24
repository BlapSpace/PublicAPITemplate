# PublicAPITemplate
The template for all public APIs




**API Ground Structur**
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
