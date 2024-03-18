import sys
from getters import *

def read():
    count = 0
    for line in sys.stdin:
        sys.stdout.write(line)
        count += 1
        if count == 10:
            break

if __name__ == "__main__":
    read()