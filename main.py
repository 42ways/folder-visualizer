#!/usr/bin/env python3
import argparse
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
    return name.replace("/", "_").replace("-", "_").replace("@", "_")


def traverse_tree(output, name):
    for dirpath, dirnames, filenames in os.walk(name):
        output.write(f'folder {canonical_name(dirpath)} as "{os.path.basename(dirpath)}"\n')
        if len(os.path.dirname(dirpath)) > 0:
            output.write(f'{canonical_name(os.path.dirname(dirpath))} -- {canonical_name(dirpath)}\n')


def main():
    parser = argparse.ArgumentParser(description='Traverse a directory tree and create an PlantUML source file '
                                                 'to visualize it graphically')
    parser.add_argument('-o', dest='output', default='folder-tree.puml',
                        help='name of output file')
    parser.add_argument('root', default='.', nargs='?',
                        help='root directory of tree traversal')
    args = parser.parse_args()
    visualise_tree(args.output, args.root)


if __name__ == '__main__':
    main()
