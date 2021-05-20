import os


def get_file_name(location):
    path_parts = location.rpartition('/')
    file_name = path_parts[2]
    return file_name

def remove_file(file_name, path):
    os.remove(f'{path}/{file_name}')
