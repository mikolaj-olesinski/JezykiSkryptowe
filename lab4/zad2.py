import os
import sys

def list_path_directories():
    print(type(os.environ.get('PATH')))
    path_dirs = os.environ.get('PATH').split(os.pathsep)
    print(type(path_dirs))
    
    for directory in path_dirs:
        print(directory)

def list_executables_in_path():
    path_dirs = os.environ.get('PATH').split(os.pathsep)
    for directory in path_dirs:
        print(f"Directory: {directory}")
        try:
            files = os.listdir(directory)
            for file in files:
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    print(f"\t{file}")
        except FileNotFoundError:
            print("\t FileNotFoundError")


if __name__ == "__main__":
    list_executables_in_path()
