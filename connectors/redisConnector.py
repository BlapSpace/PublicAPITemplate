import redis
import os

### No PANIC this is only local ###

redisIP = "0.0.0.0"
redisPort = "6379"
redisPass = "+K{#PxR.AEu(v>_KmJS7UYH<2J_ve,Ü5kgy-(Ö7Ü6bq9n6xüAr)aV)X5>aXGQ{br"

os.environ["redisIP"] = redisIP
os.environ["redisPort"] = redisPort
os.environ["redisPass"] = redisPass

###

def connect(db):
    """
    Connect to Redis with environment credentials and use the db
    """
    ### Connect to Redis ###
    try:
        redisClient = redis.Redis(host=os.environ["redisIP"],
                                                  port=os.environ["redisPort"],
                                                  password=os.environ["redisPass"],
                                                  db=db,
                                                  decode_responses=True)
    except Exception as e:
        print('[ERROR][redisConnector]: Environ "get" error')
        print(e)
        return False
    ### Connection Check Up ###
    try:
        redisClient.ping()
    except Exception as e:
        print('[ERROR][redisConnector]: Redis "connect" error')
        print(e)
        return False
    return redisClient