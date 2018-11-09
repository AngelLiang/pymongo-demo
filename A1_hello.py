# coding=utf-8
"""
https://api.mongodb.com/python/current/tutorial.html#tutorial
"""

# %%
from pymongo import MongoClient

# Getting a Database
client = MongoClient('mongodb://localhost:27017/')

# Getting a Database
db = client.hello

# Getting a Collection
user = db.user

# Getting a Document
u = user.find_one()

print(u)
