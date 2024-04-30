import sys
from helpers import graphics_ratio

def get_graphics_ratio(file=sys.stdin):
    ratio = graphics_ratio(file)
    output = f"Stosunek grafiki do wszystkich plikow: {ratio:.2f} \n\n\n"
    return output


if __name__ == "__main__":
    sys.stdout.write(get_graphics_ratio())

