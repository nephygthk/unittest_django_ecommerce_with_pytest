import pytest
from django.urls import reverse


# you dont need this mark if you are accesing the database from the factory boy
@pytest.mark.django_db
def test_store_url(client):
    url = reverse("store:store")
    response = client.get(url)
    assert response.status_code == 200


def test_categorylist_url(client, product_category):
    category = product_category
    url = reverse("store:category_list", args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200


def test_productdetail_url(client, product):
    product = product
    url = reverse("store:product_detail", args=[product.slug])
    response = client.get(url)
    assert response.status_code == 200
