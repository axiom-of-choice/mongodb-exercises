from json import load
from pymongo import MongoClient
import os
from dotenv import load_dotenv


# Requires the PyMongo package.
# https://api.mongodb.com/python/current
load_dotenv()
client = MongoClient(os.environ['MONGO_LOGIN'])

##Filters
filter={
    'id': {
        '$in': [
            '7000', '7001'
        ]
    }
}

result = client['sample_mflix']['movies'].find(
  filter=filter
)

for item in result:
    print(item)
    
