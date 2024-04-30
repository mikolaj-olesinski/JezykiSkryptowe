import sys
from helpers import biggest_resource


def get_biggest_resource(file=sys.stdin):
    path, max = biggest_resource(file)
    output = f"Sciezka do najwiekszego zasobu: {path}\nRozmiar: {max} B \n\n\n"
    return output

if __name__ == "__main__":
    sys.stdout.write(get_biggest_resource())


