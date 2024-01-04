import re

try:
    while True:
        line = input()
        while re.search('BUG',line):
            line = re.sub('BUG','',line)
        print(line)
except EOFError:
    exit()