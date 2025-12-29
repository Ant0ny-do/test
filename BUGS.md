ERROR                    [ 16%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
        r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
>       assert r.status_code == 200, r.text
E       AssertionError: {"result":{"message":"поле contacts обязательно","messages":{}},"status":"400"}
E         
E       assert 400 == 200
E        +  where 400 = <Response [400]>.status_code

conftest.py:24: AssertionError
___________________________________________________________________________________________
ERROR               [ 33%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
        r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
>       assert r.status_code == 200, r.text
E       AssertionError: {"result":{"message":"поле contacts обязательно","messages":{}},"status":"400"}
E         
E       assert 400 == 200
E        +  where 400 = <Response [400]>.status_code

conftest.py:24: AssertionError
__________________________________________________________________________________________________
ERROR          [ 50%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
        r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
>       assert r.status_code == 200, r.text
E       AssertionError: {"result":{"message":"поле contacts обязательно","messages":{}},"status":"400"}
E         
E       assert 400 == 200
E        +  where 400 = <Response [400]>.status_code

conftest.py:24: AssertionError
______________________________________________________________________________________________________
ERROR             [ 66%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
        r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
>       assert r.status_code == 200, r.text
E       AssertionError: {"result":{"message":"поле contacts обязательно","messages":{}},"status":"400"}
E         
E       assert 400 == 200
E        +  where 400 = <Response [400]>.status_code

conftest.py:24: AssertionError
____________________________________________________________________________________________________
ERROR             [ 83%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
        r = requests.post(f"{base_url}/api/1/item", json=payload, headers={"Accept": "application/json"})
>       assert r.status_code == 200, r.text
E       AssertionError: {"result":{"message":"поле contacts обязательно","messages":{}},"status":"400"}
E         
E       assert 400 == 200
E        +  where 400 = <Response [400]>.status_code

conftest.py:24: AssertionError
_____________________________________________________________________________________________________
ERROR               [100%]
test setup failed
400 != 200

Expected :200
Actual   :400
<Click to see difference>

base_url = 'https://qa-internship.avito.com', seller_id = 825736

    @pytest.fixture
    def created_item(base_url, seller_id):
        payload = {
            "sellerID": seller_id,
            "name": "QA internship test item",
            "price": 100,
            "statistics": {"likes": 1, "viewCount": 1, "contacts": 0},
        }
