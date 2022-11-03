#!/usr/bin/env python3

import sys
import re
from email.utils import parseaddr

def is_email(test_string):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return pattern.match(test_string)

# >>> parseaddr('foo@example.com')
# ('', 'foo@example.com')

# >>> parseaddr('Full Name <full@example.com>')
# ('Full Name', 'full@example.com')


def main(argv):
    try:
        test_string = argv[0]
        # test if test_string is an email address 
        print(parseaddr(test_string))
    except Exception as e:
        print('ERROR')
        print(e)
        return ''

if __name__ == '__main__':
    main(sys.argv[1:])