# File Download

The file download tool to download multiple files from the remote servers to local machine.

## Notes

- Supported protocols: HTTP(S) and FTP. There's a downloader.py file that can help to add new protocols easily.
- To avoid memory issue when the file is big, I use the streaming mechanism.
- To support download multiple files, I use the thread pool executor, so the requests can run in parallel in multiple cores machine.
- To avoid partial data, any file that is raised an exception while downloading will be removed.

## Things to improve

- Handling unique file name better. I only grab the file name by the last part of url. There are some ways to improve:

  - grouping files to folders by the domains from the urls.
  - splitting the url and concatenate to the file name.

- Allowing a user to input the destination folder. I designed the code to have an option to set the destination folder, if I can spend more time, I will handle the destination folder from user input.

- Guessing file type if the url does not have an extension of the file. There is a library named python-magic that can help to detect the file type by content of the file, but the supported file types are limited.

