# coding=utf-8
"""
创建一个collection

https://api.mongodb.com/python/current/examples/collations.html#assign-a-default-collation-to-a-collection
"""

# %%
from pymongo import MongoClient
from pymongo.collation import Collation

db = MongoClient().hello
collection = db.create_collection(
    'test_collection', collation=Collation(locale='zh'))
