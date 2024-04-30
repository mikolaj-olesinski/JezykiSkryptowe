import sys
from helpers import is_beetwen_hours

def get_data_between_hours(file=sys.stdin, start=None, end=None):

    if start is None and end is None:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
        except (IndexError, ValueError):
            print("zle wpisane godziny")
            sys.exit(1)
    elif start is None or end is None:
        raise ValueError("Wrong input")
        
    for line in file:
        if is_beetwen_hours(start, end, line):
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_between_hours()



import pytest
@pytest.mark.parametrize("start, end, expected_error", [
    (None, 12, ValueError), 
    (24, 25, ValueError),
    (-1, 12, ValueError),       
    (10, None, ValueError),    
    (10, 15, None),
    (11, 3, None),             
])
def test_get_data_between_hours(start, end, expected_error):
    file = open("NASA", "r") 
    if expected_error is not None:
        with pytest.raises(expected_error):
            get_data_between_hours(file, start=start, end=end)
    else:
        pass