import sys
from helpers import is_beetwen_hours

def get_data_between_hours(start, end):
    for line in sys.stdin:
        if is_beetwen_hours(start, end, line):
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_between_hours(22, 6)