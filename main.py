#!/usr/bin/env python3
import argparse
import os


def visualise_tree(args):
    with open(args.output, 'w') as output:
        try:
            output.writelines('@startuml\n')
            traverse_tree(output, args)
            output.write('@enduml\n')
        finally:
            output.close()


def canonical_name(name):
    return name.replace("/", "_").replace("-", "_").replace("@", "_")


def traverse_tree(output, args):
    for dir_path, dir_names, filenames in os.walk(args.root, followlinks=args.followlinks):
        output.write(f'folder {canonical_name(dir_path)} as "{os.path.basename(dir_path)}"\n')
        parent_path = os.path.dirname(dir_path)
        if len(parent_path) > 0:
            output.write(f'{canonical_name(parent_path)} -- {canonical_name(dir_path)}\n')


def main():
    parser = argparse.ArgumentParser(description='Traverse a directory tree and create an PlantUML source file '
                                                 'to visualize it graphically')
    parser.add_argument('root', default='.', nargs='?',
                        help='root directory of tree traversal')
    parser.add_argument('--follow-links', dest='followlinks', action='store_true',
                        help='follow symbolic links')
    parser.add_argument('-o', dest='output', default='folder-tree.puml',
                        help='name of output file')
    args = parser.parse_args()
    visualise_tree(args)


if __name__ == '__main__':
    main()
