import sys
from getters import get_response_code

def get_data_for_code_response(code):
    for line in sys.stdin:
        if get_response_code(line) == code:
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_for_code_response("200")

