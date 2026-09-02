import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_upload_s3_no_file():
    response = client.post("/upload-to-s3/")
    assert response.status_code == 422