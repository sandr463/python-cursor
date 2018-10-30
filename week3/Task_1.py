import os
import pprint


def print_dir(dir_path: str):
    list_dir = []

    for root, dirs, files in os.walk(dir_path):
        some_space = root.count('/')
        new_root = root.split('/')[-1]
        list_dir.append(" " * some_space + new_root)

        for name in files:
            list_dir.append(" " * some_space * 5 + "|--- " + name)

    pprint.pprint(list_dir)


dir_path = "/home/roman/CursorProjects/Test_direct"
print_dir(dir_path)
