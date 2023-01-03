# You are given a string and width
# Your task is to wrap the string into a paragraph of width 

import textwrap as t

def wrap(string, max_width):
    wrapped = t.wrap(string, max_width)
    add_newline = '\n'.join(wrapped)
    return add_newline

if __name__ == '__main__':
    string, max_width = input('Enter a String: '), int(input('Enter the Integer width to wrap to: '))
    result = wrap(string, max_width)
    print(result)