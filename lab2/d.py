import sys
from helpers import graphics_ratio

def get_graphics_ratio():
    ratio = graphics_ratio()
    output = f"Graphics to others ratio: {ratio:.2f} \n"
    sys.stdout.write(output)


if __name__ == "__main__":
    get_graphics_ratio()