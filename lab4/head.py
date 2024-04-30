import sys

def head():
    file, bytes_count, v = check_arguments_for_head()

    if not sys.stdin.isatty(): #czy przekazano dane na wejściu standardowym
        data = sys.stdin.read(bytes_count)
    else:
        if file is not None:
            with open(file, 'r') as f:
                data = f.read(bytes_count)
        else:
            print("Brak danych wejściowych.")
            sys.exit(1)

    if v:
        if file is not None:
            print(f"------------- {file} --------------")
        print(data)
    else:
        print(data)

def check_arguments_for_head():
    args = sys.argv[1:]
    file = None
    bytes = 10
    v = False

    for arg in args:

        if arg.startswith('--bytes='):
            bytes = int(arg.split('=')[1])
        elif arg == '-v':
            v = True
        elif arg.endswith('.txt'):
            file = arg
            print
        else:
            print(f"Nieprawidłowy argument: {arg}")
            sys.exit(1)

    return file, bytes, v

if __name__ == '__main__':
    head()