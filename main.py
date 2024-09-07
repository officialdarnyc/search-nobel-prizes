from fastapi import FastAPI

from pymongo import MongoClient

from typing import Optional


app = FastAPI()


# MongoDB connection details

client = MongoClient('mongodb://mongodb:27017/')

db = client['test']

collection = db['prizes']


@app.get("/search/name")

def search_name(name: Optional[str] = None):

    if name:

        query = {"laureates.firstname": {"$regex": name, "$options": "i"}}

        results = collection.find(query, {"_id": 0})

        return list(results)

    return {"error": "No name provided"}


@app.get("/search/category")

def search_category(category: Optional[str] = None):

    if category:

        query = {"category": {"$regex": category, "$options": "i"}}

        results = collection.find(query, {"_id": 0})

        return list(results)

    return {"error": "No category provided"}


@app.get("/search/description")

def search_description(motivation: Optional[str] = None):

    if motivation:

        query = {"laureates.motivation": {"$regex": motivation, "$options": "i"}}

        results = collection.find(query, {"_id": 0})

        return list(results)

    return {"error": "No description provided"}