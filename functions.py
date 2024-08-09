import os
from collections import defaultdict
import time


# func: requesting directory location
def get_user_input():
    user_input = input('Please give directory path: ')
    while True:

        if len(user_input) == 0:
            print('\nError: Directory path must be longer than 0 characters.')
            print('Please edit input and try again!')
        elif not os.path.exists(user_input):
            print('\nError: Directory path does not exist.')
            print('Please edit input and try again!')
        elif not os.path.isdir(user_input):
            print('\nError: Path leads to file, not a directory.')
            print('Please edit input and try again!')
        else:
            break
        user_input = input('\nPlease give directory path: ')
    print('Input accepted!\n')
    return user_input


# func: traversing directory location
def traverse_directory(user_input):
    duplicate_files = []
    hashmap = defaultdict(lambda: [])
    duplicate_hashes = set()
    for pathValue, _, files in os.walk(user_input):
        for file in files:
            file_location = os.path.normpath(os.path.join(pathValue, file))
            file_location = file_location.replace('\\', '/')
            f = open(file_location, 'r')
            try:
                content = hash(f.read())
            except UnicodeDecodeError:
                print('There was an error opening a file, please try a different directory. ;(')
                return []
            f.close()
            # possible option to hash files
            if len(hashmap[content]) > 0:
                duplicate_hashes.add(content)
            hashmap[content].append('./' + file_location)
    for hashes in duplicate_hashes:
        duplicate_files.append(hashmap[hashes])
    return duplicate_files
