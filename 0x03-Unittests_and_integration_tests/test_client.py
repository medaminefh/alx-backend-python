#!/usr/bin/env python3
"""test_client module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient
    """

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test org"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).org, expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google'
        )

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_repos_payload(self, org_name, expected, mock_get_json):
        """Test repos_payload"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).repos_payload, expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, expected, mock_get_json):
        """Test public_repos"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).public_repos, expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_has_license(self, org_name, expected, mock_get_json):
        """Test has_license"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).has_license, expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration GithubOrgClient
    """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, expected, mock_get_json):
        """Test public_repos"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).public_repos(), expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    @patch('client.get_json')
    def test_has_license(self, org_name, expected, mock_get_json):
        """Test has_license"""
        mock_get_json.return_value = expected
        self.assertEqual(GithubOrgClient(org_name).has_license(), expected)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/google/repos'
        )
