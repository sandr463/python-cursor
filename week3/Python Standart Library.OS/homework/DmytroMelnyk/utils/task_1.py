# Task 1
#
# Usage of os module. Create a tree of directories (any depth, any names).
# Create files in some of directories (how many. and where - up to you). Using recursive function and os module,
# pretty print the tree with directory and file names.


import os
from pprint import pprint



def treefiles(path: str):
    """
    Using recursive function and os module, pretty print the tree with directory and file names.
    :param path: 
    :return:
    """
    dictkey = {x: True for x in os.listdir(path)}
    for k, v in dictkey.items():
        if os.path.isdir(os.path.join(path, k)):
            dictkey[k] = treefiles(os.path.join(path, k))

        else:
            dictkey[k] = ''

    return dictkey


if __name__ == '__main__':
    user_path = '/mnt/48D443B7D443A5D2/Users/Melnyk.D/OneDrive/Python_Projects_education/Cursor'
    pprint(treefiles(user_path), indent=10)
