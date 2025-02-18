# Run: pytest test.py
import pytest
from pymongo import MongoClient
from ..a import f, g


@pytest.fixture
def get_db():
    TEST_MONGODB_URL = (
        "mongodb://localhost:27017/test_db"  # Replace with your test DB URL
    )
    client = MongoClient(TEST_MONGODB_URL)
    db = client.get_database()  # Or db = client["test_db"]
    collection = db["items"]  # Or db.get_collection("items")
    yield collection
    collection.delete_many({})
    client.close()


def test_do():
    y = g(1)
    assert y != 1


def test_do():
    y = f(1)
    assert y != 1


def test_insert(get_db):
    collection = get_db
    collection.insert_one({"name": "test"})
    assert collection.count_documents({}) == 1
