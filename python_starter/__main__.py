#!/usr/bin/python
"""
    python-starter: easy package creator
"""
import argparse


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='python-starter by Henri Devigne')
    arguments = parser.parse_args()

    return arguments


if __name__ == '__main__':
    main()
