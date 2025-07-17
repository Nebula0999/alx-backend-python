#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.org method"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient.org method"""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization data"""
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from org"""
        with patch.object(
            GithubOrgClient,
            "org",
            return_value={"repos_url": "https://api.github.com/orgs/test/repos"}
        ):
            client = GithubOrgClient("test")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/test/repos")
    
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repo names"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        test_url = "https://api.github.com/orgs/test/repos"

        with patch.object(
            GithubOrgClient, "_public_repos_url", return_value=test_url
        ) as mock_url:
            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(test_url)
            mock_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
