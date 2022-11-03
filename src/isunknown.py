#!/usr/bin/env python3

import sys

from internals import (
    read_file, 
    UNKNOWNS_FILE_PATH,
)

def main(argv):
    try:
        needle = argv[0]
        needle = needle.strip().lower().split()
        needle = needle[0]
        
        lines = read_file(UNKNOWNS_FILE_PATH)

        found = False
        for line in lines:
            if line.lower().strip() == needle:
                found = True
                break

        print(str(found).upper())
        
    except Exception as e:
        print('ERROR')
        print(e)
        return ''

if __name__ == '__main__':
    main(sys.argv[1:])