import pymongo

__author__ = 'ibininja'


class Database:

    URI = "mongodb://127.0.0.1:27017"
    DB = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DB = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DB[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DB[collection].find(query)

    @staticmethod
    def find_all(collection):
        return Database.DB[collection].find()

    @staticmethod
    def find_one(collection, query):
        return Database.DB[collection].find_one(query)