# Run: pytest test.py
import pytest
from pymongo import MongoClient
from a import f


def get_db():
    TEST_MONGODB_URL = (
        "mongodb://localhost:27017/test_db"  # Replace with your test DB URL
    )
    client = MongoClient(TEST_MONGODB_URL)
    db = client.get_database()  # Or db = client["test_db"]
    collection = db["items"]  # Or db.get_collection("items")
    return collection


def test_do():
    y = f(1)
    assert y != 1


def test_insert():
    collection = get_db()
    collection.insert_one({"name": "test"})
    assert collection.count_documents({}) == 1


def tset_insert_fail():
    collection = get_db()
    collection.insert_one({"name": "test"})
    assert collection.count_documents({}) == 2


def test_delete_success():
    collection = get_db()
    collection.delete_one({"name": "test"})
    assert collection.count_documents({}) == 0


def test_delete_fail():
    collection = get_db()
    collection.delete_one({"name": "test"})
    assert collection.count_documents({}) == 0
