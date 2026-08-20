import pytest
import requests

def test_get_cart_by_user(dummy_base_url):
    url = f"{dummy_base_url}/carts/user/5"

    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert 'carts' in data, "Response miss 'carts'"
    assert isinstance(data['carts'], list), "'cart' must list type"

    carts = data["carts"]
    assert len(carts) > 0, "The list do not empty"
    for cart in carts:
        assert cart["userId"] == 5, f"Cart {cart.get('id')} has userId not 5"

def test_add_new_cart(dummy_base_url):
    url = f"{dummy_base_url}/carts/add"
    payload = {
            "userId": 1,
            "products": [
                { "id": 144,"quantity": 3 },
                { "id": 98,"quantity": 2 }
            ]
        }

    response = requests.post(url, json=payload)
    assert response.status_code in [200, 201]
    data = response.json()
    assert data.get("userId") == 1
    products = data.get("products", [])
    assert len(products) == 2, f"Kỳ vọng 2 loại sản phẩm, nhưng nhận được {len(products)}"
    assert data.get("totalQuantity") == 5
    assert data.get('total') > 0
    assert data.get('discountedTotal') > 0

def test_verify_cart_financial_calculations(dummy_base_url):
     url = f"{dummy_base_url}/carts/1"

     response = requests.get(url)
     assert response.status_code == 200
     data = response.json()
     products = data.get("products", [])
     assert len(products) > 0, "Cart do not have product"

     calculated_total_quantity = sum(item["quantity"] for item in products)
     assert data.get("totalQuantity") == calculated_total_quantity, (
         f"Sai totalQuantity: Server={data.get('totalQuantity')}, Tính toán={calculated_total_quantity}"
     )

     calculated_total_price = sum(item["price"] * item["quantity"] for item in products)
     #assert data.get("total") == pytest.approx(calculated_total_price, rel=1e-2),
     assert round(data.get("total"), 2) == round(calculated_total_price, 2), (
         f"Sai total: Server={data.get('total')}, Tính toán={calculated_total_price}"
     )

     assert data.get("discountedTotal") <= data.get("total"),(
         "discountedTotal không được lớn hơn total"
     )

def test_update_cart_product_quantity(dummy_base_url):
    url = f"{dummy_base_url}/carts/1"
    payload = {
            "merge":False,
            "products": [
                {
                "id": 1,
                "quantity": 5
                }
            ]
        }

    response = requests.put(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    products = data.get("products", [])

    found = False
    for item in products:
        if item.get("id") == 1:
            assert item.get("quantity") == 5, f"Kỳ vọng quantity là 5 nhưng nhận {item.get('quantity')}"
            found = True
            break

    assert found, "Không tìm thấy sản phẩm có ID = 1 trong giỏ hàng"




    