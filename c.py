import sys
from helpers import biggest_resource


def get_biggest_resource():
    path, max = biggest_resource()
    output = f"Path to the largest resource {path}, size: {max}"
    sys.stdout.write(output)

if __name__ == "__main__":
    get_biggest_resource()