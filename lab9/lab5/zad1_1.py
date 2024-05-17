import re
from datetime import datetime
from typing import Optional

def read_file(file: Optional[str] = None):
    if file is None:
        file = input("Enter file name: ")
    
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()

def read_log(log: str) -> Optional[tuple]:
    pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\w+)\s+(\w+)\[(\d+)\]:\s+(.*)'
    date_pattern = '%b %d %H:%M:%S'
    
    line: Optional[tuple] = None
    match = re.match(pattern, log)
    if match:
        date_str, host_name, app_component, PID_number, description = match.groups()
        date = datetime.strptime(date_str, date_pattern)
        description = description.strip()
        line = (date, host_name, app_component, int(PID_number), description)
    else:
        line = ()  # Zwracamy pustą krotkę, jeśli nie udało się dopasować wzorca
    return line

def get_ipv4s_from_log(log_description: str) -> list[str]:
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b' 
    ipv4_addresses = re.findall(ipv4_pattern, log_description)
    return ipv4_addresses

def get_user_from_log(log_description: str) -> Optional[str]:
    user_pattern = r'user \w+'
    users = re.search(user_pattern, log_description)
    return users.group().split()[-1] if users else None

def get_user(log_description: str) -> Optional[str]:
    user_pattern = r'user (\S+)'
    second_user_pattern = r'for (\S+)'
    users = re.search(user_pattern, log_description)

    if users:
        return users.group(1)
    else:
        users = re.search(second_user_pattern, log_description)
    
    return users.group(1) if users else None

def get_message_type(log_description: str) -> str:
    success_login_pattern = r'session opened for user'
    failed_login_pattern = r'Failed password for'
    connection_closed_pattern = r'session closed for user'
    incorrect_password_pattern = r'authentication failure'
    incorrect_username_pattern = r'Invalid user'
    intrusion_attempt_pattern = r'POSSIBLE BREAK-IN ATTEMPT!'
    error_pattern = r'error: '
    accepted_password_pattern = r'Accepted password for'
    
    if re.search(success_login_pattern, log_description):
        return "Successful login"
    elif re.search(failed_login_pattern, log_description):
        return "Failed login"
    elif re.search(connection_closed_pattern, log_description):
        return "Connection closed"
    elif re.search(incorrect_password_pattern, log_description):
        return "Incorrect password"
    elif re.search(incorrect_username_pattern, log_description):
        return "Incorrect username"
    elif re.search(intrusion_attempt_pattern, log_description):
        return "Break-in attempt"
    elif re.search(error_pattern, log_description):
        return "Error"
    elif re.search(accepted_password_pattern, log_description):
        return "Accepted password"
    else:
        return "Other"

if __name__ == "__main__":
    for log in read_file():
        log = read_log(log)
        print(log)
