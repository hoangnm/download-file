import requests
import ftplib
from file_utils import get_file_name

class BaseDownloader:
    def __init__(self, url, url_parts, destination_folder='files'):
        self.file_name = get_file_name(url_parts.path)
        self.url = url
        self.url_parts = url_parts
        self.destination_folder = destination_folder

    def open(self):
        return open(f'{self.destination_folder}/{self.file_name}', 'w')


class HttpDownloader(BaseDownloader):
    def download(self):
        response = requests.get(self.url, stream=True)
        with self.open() as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)


class FtpDownloader(BaseDownloader):
    def download(self):
        ftp = ftplib.FTP(self.url_parts.hostname,
                         self.url_parts.username, self.url_parts.password)
        ftp.encoding = 'utf-8'
        with self.open() as f:
            ftp.retrbinary(f'RETR {self.file_name}', f.write)
        ftp.quit()


def get_downloader(url, url_parts):
    scheme = url_parts.scheme
    if scheme == 'http' or scheme == 'https':
        return HttpDownloader(url, url_parts)
    elif scheme == 'ftp':
        return FtpDownloader(url, url_parts)
