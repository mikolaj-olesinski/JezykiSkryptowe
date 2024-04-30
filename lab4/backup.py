import os
import zipfile
import json
import datetime
import sys

def create_backup(source_dir):
    backup_dir = create_backup_dir()
    backup_path = create_backup_archive(source_dir, backup_dir)
    update_backup_history(backup_dir, source_dir, backup_path)
    print(f"Backup created successfully: {os.path.basename(backup_path)}")
    print(f"Backup saved to: {backup_path}")

def create_backup_dir():
    backup_dir = os.getenv('BACKUPS_DIR', os.path.join(os.path.expanduser('~'), '.backups'))
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    return backup_dir

def create_backup_archive(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    dirname = os.path.basename(source_dir)
    backup_filename = f"{timestamp}-{dirname}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)

    with zipfile.ZipFile(backup_path, 'w') as backup_zip:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                backup_zip.write(file_path, os.path.relpath(file_path, source_dir))

    return backup_path #zwrocenie sciezki do pliku by potem dodac do historii

def update_backup_history(backup_dir, source_dir, backup_path):
    timestamp = os.path.basename(backup_path).split('-')[0]
    backup_info = {
        'date': timestamp,
        'source_dir': os.path.abspath(source_dir),
        'backup_filename': os.path.basename(backup_path)
    }

    backup_history_file = os.path.join(backup_dir, 'backup_history.json')
    if os.path.exists(backup_history_file):
        with open(backup_history_file, 'r') as f:
            backup_history = json.load(f)
        backup_history.append(backup_info)
        with open(backup_history_file, 'w') as f:
            json.dump(backup_history, f, indent=4)
    else:
        with open(backup_history_file, 'w') as f:
            json.dump([backup_info], f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("zle argumenty")
        sys.exit(1)

    source_dir = sys.argv[1]
    create_backup(source_dir)
