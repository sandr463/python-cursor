from utils.task_1 import gen_tree, dir_tree
from utils.task_2 import dict_to_csv
from utils.task_3 import get_data

if __name__ == "__main__":
    import os
    from pprint import pprint

    from utils.data import group_list

    # Task 1
    ROOT = os.path.expandvars('/home/$USER/sample/')
    TREE = {'file': '',
            'folder1': {'file1': '', 'file2': '', 'subfolder': {'file': ''}},
            'folder2': {'file1': ''},
            'folder3': {}}

    gen_tree(ROOT, TREE)
    pprint(dir_tree(ROOT))

    # Task 2
    dict_to_csv(group_list)

    # Task 3
    get_data('https://dummyimage.com/600x400/000/fff')
