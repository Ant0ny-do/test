import requests

def test_post_item_success(created_item):
    assert created_item["id"]
    assert "createdAt" in created_item

def test_get_item_by_id_success(base_url, created_item):
    item_id = created_item["id"]
    r = requests.get(f"{base_url}/api/1/item/{item_id}", headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text
    data = r.json()
    assert isinstance(data, list)
    assert any(x.get("id") == item_id for x in data)

def test_get_items_by_seller_success(base_url, created_item):
    seller_id = created_item["sellerId"]
    r = requests.get(f"{base_url}/api/1/{seller_id}/item", headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text
    data = r.json()
    assert isinstance(data, list)
    assert all(x.get("sellerId") == seller_id for x in data)

def test_get_statistic_v1_success(base_url, created_item):
    item_id = created_item["id"]
    r = requests.get(f"{base_url}/api/1/statistic/{item_id}", headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text
    data = r.json()
    assert isinstance(data, list)
    for row in data:
        for k in ("likes", "viewCount", "contacts"):
            assert isinstance(row.get(k), int)
            assert row[k] >= 0

def test_get_statistic_v2_success(base_url, created_item):
    item_id = created_item["id"]
    r = requests.get(f"{base_url}/api/2/statistic/{item_id}", headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text

def test_delete_item_v2_success(base_url, created_item):
    item_id = created_item["id"]
    r = requests.delete(f"{base_url}/api/2/item/{item_id}", headers={"Accept": "application/json"})
    assert r.status_code == 200, r.text
    assert r.text == ""  # в коллекции для 200 body пустой
