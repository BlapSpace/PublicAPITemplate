import pymongo
import os

def connect():
    """
    Connect to MongoDB with environment credentials
    """
    ### Connect to MongoDB ###
    mongodbClient = pymongo.MongoClient(host=os.environ["mongoDBIP"],
                                                                           username=os.environ["mongoDBUsername"],
                                                                           password=os.environ["mongoDBPassword"],
                                                                           authSource=os.environ["mongoDBAuthSource"],
                                                                           authMechanism=os.environ["mongoDBAuthMechanism"])
    ### Connection Check Up ###
    try:
        mongodbClient.server_info()
    except Exception as e:
        print('[ERROR][mongoDBConnector]: MongoDB "connect" error')
        print(e)
        #exit()
    return mongodbClient