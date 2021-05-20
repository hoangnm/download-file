from urllib.parse import urlparse
import concurrent.futures
from file_utils import remove_file, get_file_name
from downloader import get_downloader



class FileDownload:
    def __init__(self, downloader):
        self.downloader = downloader

    def download(self):
        try:
            self.downloader.download()
            return f'{self.downloader.file_name}'
        except:
            remove_file(self.downloader.file_name,
                        self.downloader.destination_folder)
            raise


def get_files_input():
    urls = []
    while True:
        url = input(
            "Enter an url to download or an empty space to finish input: ")
        if url == '':
            break
        urls.append(url)
    return urls




def main():
    urls = get_files_input()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            url_parts = urlparse(url)
            downloader = get_downloader(url, url_parts)
            fileDownload = FileDownload(downloader)
            futures.append(executor.submit(fileDownload.download))

        for future in concurrent.futures.as_completed(futures):
            try:
                file_name = future.result()
                print(f'{file_name} is downloaded')
            except Exception:
                print(f'error on {file_name}')


if __name__ == "__main__":
    main()
