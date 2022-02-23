#!/usr/bin/env python3
# Traverse a directory tree and create an PlantUML source file to visualize it
import sys
import os


def visualise_tree(filename, name):
    with open(filename, 'w') as output:
        try:
            output.writelines('@startuml\n')
            traverse_tree(output, name)
            output.write('@enduml\n')
        finally:
            output.close()


def canonical_name(name):
    return name.replace("/", "_").replace("-", "_")


def traverse_tree(output, name):
    for dirpath, dirnames, filenames in os.walk(name):
        output.write(f'folder {canonical_name(dirpath)} as "{os.path.basename(dirpath)}"\n')
        if len(os.path.dirname(dirpath)) > 0:
            output.write(f'{canonical_name(os.path.dirname(dirpath))} -- {canonical_name(dirpath)}\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = "."
    visualise_tree('folder-tree.puml', root)
