from pymongo import MongoClient
#import redis

MONGODB_DB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME = 'appium_db'
client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]


#redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

#r = redis.StrictRedis(host='localhost', port=6379, db=0)