from elasticsearch import Elasticsearch
from ssl import create_default_context
import os

def connect():
    """
    Connect to ElasticSearch with environment credentials
    """
    ### Connect to Elasticsearch ###
    context = create_default_context(cafile=None)
    esClient = Elasticsearch(hosts=os.environ["elasticsearchHosts"],
                                              http_auth=os.environ["elasticsearchHttpAuth"],
                                              scheme=os.environ["elasticsearchScheme"],
                                              port=os.environ["elasticsearchPort"],
                                              ssl_context=context)
    ### Connection Check Up ###
    if esClient.ping() != True:
        print('[ERROR][elasticsearchConnector]: ElasticSearch "connect" error')
        #exit()
    return esClient
