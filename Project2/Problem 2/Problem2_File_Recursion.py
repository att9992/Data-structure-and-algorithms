import os

def find_files(suffix,path):
    if suffix == '':
        return []
    if len(os.listdir(path)) == 0:
        return []
    list_file = os.listdir(path)
    path_files = [file for file in list_file if '.' + suffix in file]
    path_folders = [folder for folder in list_file if '.' not in folder] 

    for folder in path_folders:
        path_files.extend(find_files(suffix = suffix, path = path + '/' +folder))
    return path_files


