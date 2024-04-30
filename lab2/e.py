import sys
from getters import get_response_code

def get_data_for_code_response(file=sys.stdin, code=None):

    if code is None:
        try:
            code = sys.argv[1]
        except IndexError:
            print("zle wpisany kod")
            sys.exit(1)

    for line in file:
        if get_response_code(line) == code:
            sys.stdout.write(line)

if __name__ == "__main__":
    get_data_for_code_response()

