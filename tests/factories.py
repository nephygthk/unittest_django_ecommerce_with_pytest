import factory
from faker import Faker

from ecommerce.apps.store.models import (
    Category,
    Product,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

faker = Faker()

# #####
# store
# #####


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "phone"
    slug = "phone"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
        django_get_or_create = ("name",)

    name = "samsung"


class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "series"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = "galaxy_s9"
    description = faker.text()
    slug = "galaxy_s9"
    regular_price = "18000.00"
    discount_price = "140000.00"


class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = "s_series"
