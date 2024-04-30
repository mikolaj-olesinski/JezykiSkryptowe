from helpers import count_codes
import sys

def count_lines_with_code(code=None, file=sys.stdin):
    
    if code is None:
        try:
            code = sys.argv[1]
        except IndexError:
            print("zle wpisany kod")
            sys.exit(1)

    output = f"Liczba linii z kodem {code}: wynosi {count_codes(code, file)} \n\n\n"
    return output
    

if __name__ == "__main__":
    sys.stdout.write(count_lines_with_code())



import pytest

@pytest.mark.parametrize(
    "code, expected_output", 
    [
        ("200", "Liczba linii z kodem 200: wynosi 1701534 \n\n\n"),
        ("302", "Liczba linii z kodem 302: wynosi 46573 \n\n\n"),
        ("500", "Liczba linii z kodem 500: wynosi 62 \n\n\n"),
        ("312312", "Liczba linii z kodem 312312: wynosi 0 \n\n\n"),
        ("a", "Liczba linii z kodem a: wynosi 0 \n\n\n"),
    ]
)
def test_count_lines_with_code(code, expected_output):
    file = open("NASA", "r") 
    assert count_lines_with_code(code, file) == expected_output


