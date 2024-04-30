import sys
from getters import get_host_domain

def find_data_for_domain(domain=None, file=sys.stdin):

    if domain is None:
        try:
            domain = sys.argv[1]
        except (IndexError):
            print("zle wpisana domena")
            sys.exit(1)
            
    for line in file:
        if get_host_domain(line) == domain:
            sys.stdout.write(line)

if __name__ == "__main__":
    find_data_for_domain()