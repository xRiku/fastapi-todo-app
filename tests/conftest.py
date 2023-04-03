import pytest
from db.memory import db
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture()
def reset_db():
    db.wipe()


@pytest.fixture()
def client():
    return TestClient(app)
