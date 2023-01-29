# from django.test import TestCase


# class MyTestClass(TestCase):
#     def test_hello_world(self):
#         self.assertEqual("Hello", "Hello")
import pytest


def test_hello_world1(text_fixture1):
    print("fucntion 1")
    assert text_fixture1 == 1


def test_hello_world2(text_fixture1):
    print("fucntion 2")
    assert text_fixture1 == 1
