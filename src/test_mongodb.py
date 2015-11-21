__author__='ibrahim Mokdad'

import pymongo

uri="mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['NewsTest']
collection= database['Posts']
news=collection.find({})
print(news)

for article in news:
    print (article)

news=collection.remove({"The craze of the world"})