import os
import random
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://qa-internship.avito.com")

@pytest.fixture(scope="session")
def seller_id():
    # диапазон из задания (чтобы снизить пересечения) [file:2]
    return int(os.getenv("SELLER_ID", str(random.randint(111111, 999999))))

@pytest.fixture
def created_item(base_url, seller_id):
    payload = {
        "sellerID": seller_id,
        "name": "QA internship test item",
        "price": 100,
        "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
    }
    r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text
    data = r.json()
    assert "id" in data
    return data
