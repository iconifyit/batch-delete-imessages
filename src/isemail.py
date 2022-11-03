#!/usr/bin/env python3

import sys
import re
from email.utils import parseaddr

from internals import (
    is_email, 
)

def main(argv):
    try:
        test_string = argv[0]
        print(str(is_email(test_string)).upper())
    except Exception as e:
        print('FALSE')
        # print(e)
        return ''

if __name__ == '__main__':
    main(sys.argv[1:])