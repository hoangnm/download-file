# File Download
The file download tool to download multiple files from the remote servers to local machine.

* Supported protocols: HTTP(S) and FTP. There's a downloader.py file that can help to support new protocols easily.
* To avoid memory issue when the file is big, I use the streaming mechanism.
* To support download multiple files, I use the thread pool executor, so the requests can run parallel in multiple cores machine.
* To avoid partial data, any file that is raised an exception while downloading will be removed.

