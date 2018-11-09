# coding=utf-8

# %%
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# Database: hello
# Collection: user
User = client.hello.user
q = {"_id": 1}
u = User.find_one(q)

print(u)
