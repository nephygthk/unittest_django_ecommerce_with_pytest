import factory
from faker import Faker

from ecommerce.apps.account.models import Address, Customer
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


# ####
# account
# #####


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = "a@a.com"
    full_name = "user1"
    phone_number = "07525251252"
    password = "tester"
    is_active = True
    is_staff = False


@classmethod
def _create(cls, model_class, *args, **kwargs):
    manager = cls._get_manager(model_class)
    if "is_superuser" in kwargs:
        return manager.create_superuser(*args, **kwargs)
    else:
        return manager.create_user(*args, **kwargs)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    customer = factory.SubFactory(CustomerFactory)
    full_name = faker.name()
    phone = faker.phone_number()
    postcode = faker.postcode()
    address_line = faker.street_address()
    address_line2 = faker.street_address()
    town_city = faker.city_suffix()
