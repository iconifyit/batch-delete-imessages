#!/usr/bin/env python3

import os
import pathlib
import re
import string
import sys
from email.utils import parseaddr

KEY_UNKNOWNS = 'UNKNOWNS'
KEY_PEOPLE = 'PEOPLE'
KEY_PHONES = 'PHONES'

ROOT_DIR = pathlib.Path(__file__).parent.absolute().resolve()
UNKNOWNS_FILE_PATH = "{}{}".format(ROOT_DIR, '/unknowns')
PEOPLE_FILE_PATH = "{}{}".format(ROOT_DIR, '/people')
PHONES_FILE_PATH = "{}{}".format(ROOT_DIR, '/phones')

def is_email(test_string):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    matches = pattern.match(test_string)
    if matches:
        return True
    else:
        return False

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return ''

def digits_only(line):
    return "00000000{}".format(''.join([i for i in line if i.isdigit()]))
