#!/usr/bin/env python3

import sys

from internals import (
    read_file, 
    PEOPLE_FILE_PATH,
    PHONES_FILE_PATH,
)

def main(argv):
    try:
        needle = argv[0]
        needle = needle.strip().lower().split()
        needle = needle[0]
        
        people = read_file(PEOPLE_FILE_PATH)
        phones = read_file(PHONES_FILE_PATH)
        lines = people + phones

        found = False
        for line in lines:
            if needle in line.lower().strip():
                found = True
                break

        print(str(found).upper())
        
    except Exception as e:
        print('ERROR')
        print(e)
        return ''

if __name__ == '__main__':
    main(sys.argv[1:])