import requests_mock
import unittest
from urllib.parse import urlparse
from unittest.mock import patch, mock_open
from downloader import HttpDownloader


class TestHttpDownloader(unittest.TestCase):
    def test_download(self):
        """
        Test that it can download a file from http
        """
        url = 'http://test.com/file.js'
        url_parts = urlparse(url)
        downloader = HttpDownloader(url, url_parts)
        return_value = {
            'test': 101,
        }
        with requests_mock.Mocker() as rm:
            with patch(url, mock_open()) as mocked_file:
                rm.get(url,
                        json=return_value, status_code=200)
                downloader.download()
                mocked_file.assert_called_once_with(url, 'wbr')

if __name__ == '__main__':
    unittest.main()
