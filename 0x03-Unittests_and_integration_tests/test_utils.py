#!/usr/bin/env python3
"""
test_utils module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
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
