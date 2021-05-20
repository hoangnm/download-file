from urllib.parse import urlparse
import requests_mock
import json
import unittest
from unittest.mock import patch, mock_open
from downloader import HttpDownloader


class TestHttpDownloader(unittest.TestCase):
    def test_download(self):
        """
        Test download a file from http
        """
        file_name = 'file.js'
        url = f'http://test.com/{file_name}'
        url_parts = urlparse(url)
        downloader = HttpDownloader(url, url_parts)
        return_value = {
            'test': 101,
        }
        with requests_mock.Mocker() as rm:
            with patch('downloader.open', mock_open()) as mocked_file:
                rm.get(url,
                        json=return_value, status_code=200)
                downloader.download()
                mocked_file.assert_called_once_with(f'{downloader.destination_folder}/{file_name}', 'w')
                mocked_file().write.assert_called_once_with(json.dumps(return_value).encode())

if __name__ == '__main__':
    unittest.main()
