import pytest
import requests

def test_get_products_with_pagination(dummy_base_url):
    url = f"{dummy_base_url}/products?limit=10&skip=10&select=title,price,category"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    products = data.get('products', [])

    assert len(products) == 10
    assert data.get("total") > 0
    assert data.get("skip") == 10

    require_fields = ["title", "price", "category"]
    for product in products:
        for field in require_fields:
            assert field in product, f"Trường '{field}' bị thiếu trong sản phẩm id {product.get('id')}"

def test_search_products_by_keyword(dummy_base_url):
    url = f"{dummy_base_url}/products/search?q=phone"

    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    products = data.get('products', [])

    assert len(products) > 0
    for product in products:
        title = product.get("title","").lower()
        description = product.get("description", "").lower()
        assert "phone" in title or "phone" in description, f"Không tìm thấy 'phone' trong sản phẩm id {product.get('id')}"

def test_filter_products_by_category(dummy_base_url):
    url = f"{dummy_base_url}/products/category/smartphones" 

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    products = data.get('products', []) 

    assert len(products) > 0
    for product in products:
        category = product.get('category',"").lower()
        assert "smartphones" in category, f"Không tìm thấy 'Smart Phone' trong sản phẩm id {product.get('id')} "

def test_get_product_not_found(dummy_base_url):
    url = f"{dummy_base_url}/products/99999"

    response = requests.get(url)

    assert response.status_code == 404
    assert response.json()["message"] == "Product with id '99999' not found"
