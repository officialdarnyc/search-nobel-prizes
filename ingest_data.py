import requests
import pymongo
import json

# MongoDB connection details
MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
DB_NAME = 'test'
COLLECTION_NAME = 'prizes'

# URL to download the dataset
DATASET_URL = 'https://api.nobelprize.org/v1/prize.json'

def download_data(url):
    """Download data from the provided URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def insert_data_into_mongo(data, collection):
    """Insert data into MongoDB collection."""
    collection.insert_many(data['prizes'])  # Insert documents into the collection

def main():
    # Download the dataset
    data = download_data(DATASET_URL)

    # Connect to MongoDB
    client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Clear the collection before inserting new data
    collection.drop()

    # Insert data into MongoDB
    insert_data_into_mongo(data, collection)
    print("Data successfully ingested into MongoDB.")

if __name__ == '__main__':
    main()
