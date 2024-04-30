import sys
from helpers import get_day_of_week

def get_data_for_day(file=sys.stdin, day=None):

    if day is None:
        try:
            day = int(sys.argv[1])
        except (IndexError):
            print("zle wpisany dzien")
            sys.exit(1)

    if day < 1 or day > 7:
        raise ValueError("Wrong day")

    for line in file:
        if get_day_of_week(line) == day - 1:
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_for_day()


import pytest
@pytest.mark.parametrize("day, expected_error", [
    (0, ValueError),
    (8, ValueError),
    (-1, ValueError),
    (1, None),
    (2, None),
    (7, None),
])
def test_get_data_for_day(day, expected_error):
    file = open("NASA", "r")
    if expected_error is not None:
        with pytest.raises(expected_error):
            get_data_for_day(file, day=day)
    else:
        pass