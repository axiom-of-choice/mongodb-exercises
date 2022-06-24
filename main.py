from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://axiom-of-choice:458Wo8qMfM55l80t@cluster0.epz53.mongodb.net/test')
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