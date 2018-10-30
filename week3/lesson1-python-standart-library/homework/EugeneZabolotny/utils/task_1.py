import os


def gen_tree(root: str, tree: dict):
    for name, value in tree.items():
        if isinstance(value, dict):
            os.makedirs(os.path.join(root, name), exist_ok=True)
            gen_tree(os.path.join(root, name), value)
        else:
            open(os.path.join(root, name), 'w+')


def dir_tree(path: str):
    for root, dirs, files in os.walk(path):
        tree = {d: dir_tree(os.path.join(root, d)) for d in dirs}
        tree.update({f: '' for f in files})
        return tree


if __name__ == '__main__':
    from pprint import pprint

    ROOT = os.path.expandvars('/home/$USER/sample/')
    TREE = {'file': '',
            'folder1': {'file1': '', 'file2': '', 'subfolder': {'file': ''}},
            'folder2': {'file1': ''},
            'folder3': {}}

    gen_tree(ROOT, TREE)
    pprint(dir_tree(ROOT))
