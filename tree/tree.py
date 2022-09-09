from os import listdir, getcwd
from os.path import isdir, join

__all__ = ['tree_sort_by_extension', 'tree_sort_by_filename', 'tree_no_sorting']

def sort_key(x):
    if '.' in x:
        return x.split('.')[-1]
    return '.'

def tree_sort_by_extension(path=getcwd(), indent=0):
    print(indent*' ' + '|-', path.split('/')[-1])
    for file in sorted(listdir(path), key=sort_key):
        if isdir(join(path, file)):
            tree_sort_by_extension(join(path, file), indent+2)
        else:
            print('  ' + indent*' ' + '|-', file)

def tree_sort_by_filename(path=getcwd(), indent=0):
    print(indent*' ' + '|-', path.split('/')[-1])
    for file in sorted(listdir(path)):
        if isdir(join(path, file)):
            tree_sort_by_filename(join(path, file), indent+2)
        else:
            print('  ' + indent*' ' + '|-', file)

def tree_no_sorting(path=getcwd(), indent=0):
    print(indent*' ' + '|-', path.split('/')[-1])
    for file in listdir(path):
        if isdir(join(path, file)):
            tree_no_sorting(join(path, file), indent+2)
        else:
            print('  ' + indent*' ' + '|-', file)
