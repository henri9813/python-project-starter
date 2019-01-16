#!/usr/bin/python
"""
    tar-progress: monitor tool for tar process
"""
import platform
import argparse
from tar_progress.classes import interface, linux, windows


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='python-starter by Henri Devigne')
    arguments = parser.parse_args()

    print(arguments)


if __name__ == '__main__':
    main()
