#!/usr/bin/python
"""
    python-project-starter: easy package creator
"""
import argparse
import shutil
import os


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='python-project-starter by Henri Devigne')

    parser.add_argument('path',
                        action="store",
                        type=str,
                        help="Path where the project will be create",
                        default=".")
    parser.add_argument('-n', '--name',
                        action="store",
                        type=str,
                        help="Name of the project",
                        default=None)
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help="Enable verbosity",
                        default=False)

    arguments = parser.parse_args()

    try:
        # see https://github.com/PyCQA/pylint/issues/2696
        # pylint: disable=C0321
        if arguments.verbose: print("Cloning template into: " + arguments.path)
        shutil.copytree(
            os.path.dirname(os.path.realpath(__file__)) + "/template",
            arguments.path
        )
    except OSError:
        print("Unable to create project in: " + arguments.path)
        return -1

    module_directory = os.path.basename(arguments.path) if not arguments.name else arguments.name

    os.rename(
        arguments.path + "/my_project",
        arguments.path + "/" + module_directory
    )

    return 0


if __name__ == '__main__':
    main()
