import os
import zipfile
import json
import sys

def load_backup_history(backup_dir):
    backup_history_file = os.path.join(backup_dir, 'backup_history.json')
    if not os.path.exists(backup_history_file):
        print("No backup history found.")
        sys.exit(1)

    with open(backup_history_file, 'r') as f:
        return json.load(f)

def display_backup_history(backup_history):
    print("Backup History:")
    for i, backup_info in enumerate(backup_history, 1):
        print(f"{i}. Date: {backup_info['date']}, Source Directory: {backup_info['source_dir']}, Backup Filename: {backup_info['backup_filename']}")

def get_backup_choice(backup_history):
    choice = input("Enter the number of the backup you want to restore: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(backup_history):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice.")
        sys.exit(1)

def restore_backup(backup_dir, restore_dir, choice, backup_history):
    backup_info = backup_history[choice - 1] 
    backup_filename = backup_info['backup_filename']
    backup_path = os.path.join(backup_dir, backup_filename)


    if not os.path.exists(restore_dir):
        print(f"Directory '{restore_dir}' does not exist.")
        sys.exit(1)

    # Usuń zawartość source katalogu
    for root, dirs, files in os.walk(restore_dir):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

    with zipfile.ZipFile(backup_path, 'r') as backup_zip:
        backup_zip.extractall(restore_dir)

    print("Backup restored successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        restore_dir = os.getcwd()  # Użyj bieżącego katalogu roboczego
    else:
        restore_dir = sys.argv[1]

    backup_dir = os.getenv('BACKUPS_DIR', os.path.join(os.path.expanduser('~'), '.backups'))

    backup_history = load_backup_history(backup_dir)
    display_backup_history(backup_history)
    choice = get_backup_choice(backup_history)
    restore_backup(backup_dir, restore_dir, choice, backup_history)
