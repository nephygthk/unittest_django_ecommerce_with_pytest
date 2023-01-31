import pytest
from django.urls import reverse


def test_category_str(product_category):
    assert product_category.__str__() == "phone"


def test_category_absolute_url(client, product_category):
    category = product_category
    url = reverse("store:category_list", args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200


def test_product_type_str(product_type):
    assert product_type.__str__() == "samsung"


def test_product_spec_str(product_specification):
    assert product_specification.__str__() == "series"


def test_product_str(product):
    assert product.__str__() == "galaxy_s9"


def test_product_absolute_url(client, product):
    product = product
    url = reverse("store:product_detail", args=[product.slug])
    response = client.get(url)
    assert response.status_code == 200


def test_product_spec_value_str(product_spec_value):
    assert product_spec_value.__str__() == "s_series"
