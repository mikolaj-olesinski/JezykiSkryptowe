import sys
from getters import get_host_domain

def find_data_for_domain(domain):
    for line in sys.stdin:
        if get_host_domain(line) == domain:
            sys.stdout.write(line)

if __name__ == "__main__":
    find_data_for_domain("pl")