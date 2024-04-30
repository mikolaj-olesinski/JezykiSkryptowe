import os
import sys

def print_env_variables():
    for env_var in sorted(os.environ):
        print(env_var)

def print_env_variables_from_sys():
    data = sorted(sys.argv[1:])

    for env_var in data:
        if env_var in os.environ:
            print(env_var)


if __name__ == '__main__':
    
    #Aby uruchomic zad1.1
    print_env_variables()

    #Aby uruchomic zad 1.2
    print_env_variables_from_sys

    


# PATH HOME LANG USER