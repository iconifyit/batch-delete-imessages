#!/usr/bin/env python3

import sys
import pathlib
import os 
import string

from internals import (
    read_file, 
    KEY_UNKNOWNS, 
    KEY_PEOPLE, 
    KEY_PHONES, 
    digits_only, 
    UNKNOWNS_FILE_PATH,
    PEOPLE_FILE_PATH,
    PHONES_FILE_PATH,
)

def main(argv):
    try:
        which_file = argv[0]
        which_file = which_file.strip().upper().split()
        which_file = which_file[0]

        if KEY_UNKNOWNS in which_file:
            file_path = UNKNOWNS_FILE_PATH
        elif KEY_PEOPLE in which_file:
            file_path = PEOPLE_FILE_PATH
        elif KEY_PHONES in which_file:
            file_path = PHONES_FILE_PATH
        else:
            raise Exception('ERROR: Unknown file name')
        
        lines = read_file(file_path)

        values = []
        for line in lines:
            newline = line
            if which_file == KEY_UNKNOWNS:
                newline = digits_only(line)[-8:] 
            values.append(newline.strip().lower())

        print(" ".join(values))
        
    except Exception as e:
        print('ERROR')
        print(e)
        return ''

if __name__ == '__main__':
    main(sys.argv[1:])