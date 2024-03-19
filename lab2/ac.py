from helpers import count_codes
import sys

def count404():
    sys.stdout.write(str(count_codes("404")) + "\n")

if __name__ == "__main__":
    count404()