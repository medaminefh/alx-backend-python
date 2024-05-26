#!/usr/bin/env python3
"""
test_utils module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """Test access_nested_map exception"""
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map_with_mocks(self, nested_map, path, expected):
        """Test access_nested_map with mocks"""
        mock = Mock()
        mock.return_value = expected
        with patch('utils.access_nested_map', mock):
            self.assertEqual(access_nested_map(nested_map, path), expected)

        mock.assert_called_once_with(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, expected: Any) -> None:
        """Test get_json"""
        self.assertEqual(get_json(url), expected)

    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False}),
    ])
    def test_get_json_with_mocks(self, url, expected):
        """Test get_json with mocks"""
        mock = Mock()
        mock.return_value = expected
        with patch('utils.get_json', mock):
            self.assertEqual(get_json(url), expected)

        mock.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """TestClass class"""

            def a_method(self):
                """a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property property"""
                return self.a_method()

        test = TestClass()

        self.assertEqual(test.a_property, 42)

        with self.assertRaises(TypeError):
            test.a_property = 42

        self.assertEqual(test.a_property, 42)
