#!/usr/bin/env python3
"""
Module to parameterize a unittest
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test access nested map Class representation """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests that the method returns correct result """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that KeyError is raised for inputs (use @parameterized.expand)
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests that utils.get_json returns the expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Tests that the get_json method returns correct result
        """
        class Mocked(Mock):
            """
            Mocked class representation
            """

            def json(self):
                """
                Returns payload
                """
                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ Memoize unittest  class representation"""

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Tests class """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
