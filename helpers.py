from getters import *

def count_codes(code):
    counter = 0
    for line in sys.stdin:
        if get_response_code(line) == code:
            counter += 1
    return counter


def sum_data():
    total_data = 0
    for line in sys.stdin:
        data = get_bytes(line)
        if get_request(line) == "GET" and data != "-":
            total_data += int(get_bytes(line))
    return total_data


def biggest_resource():
    max = 0
    path = ""
    for line in sys.stdin:
        bytes = get_bytes(line)
        if bytes.isdigit() and int(bytes) > max:
            max = int(bytes)
            path = get_path(line)
    return (path, max)

