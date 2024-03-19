import sys
from helpers import get_day_of_week

def get_data_for_day(day):
    for line in sys.stdin:
        if get_day_of_week(line) == day:
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_for_day(4)