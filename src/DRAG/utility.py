import os

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower().lstrip('.')
    return file_extension