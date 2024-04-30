import typer
import zad1_1
import zad1_2
import zad1_3
import zad1_dodatkowe
from enum import Enum

class LogLevels(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    CRITICAL = "CRITICAL"

app = typer.Typer(help="SSH log analyzer")
logfile_path = {"path": "SSH.log"}

@app.command('task_1_1_1')
def task_1_1_1(file: str, log_number: int):
    """
    Get a specific log entry from the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        log_number (int): The number of the log entry to retrieve.
    """
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(log)
            return
        else:
            i += 1
    print("Invalid log number")

@app.command('task_1_1_2')
def task_1_1_2(file: str, log_number: int):
    """
    Get IPv4 addresses from a specific log entry in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        log_number (int): The number of the log entry to analyze.
    """
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_ipv4s_from_log(log[-1]))
            return
        else:
            i += 1
    print("Invalid log number")

@app.command('task_1_1_3')
def task_1_1_3(file: str, log_number: int):
    """
    Get the username from a specific log entry in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        log_number (int): The number of the log entry to analyze.
    """
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_user_from_log(log[-1]))
            return
        else:
            i += 1
    print("Invalid log number")


@app.command('task_1_1_4')
def task_1_1_4(file: str, log_number: int):
    """
    Get the message type from a specific log entry in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        log_number (int): The number of the log entry to analyze.
    """
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_message_type(log[-1]))
            return
        else:
            i += 1
    print("Invalid log number")

@app.command('task_1_2')
def task_1_2(file: str, log_level: LogLevels, log_number: int):
    """
    Get the logger type for a specific log entry in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        log_level (LogLevels): The minimum logging level.
        log_number (int): The number of the log entry to analyze.
    """
    i = 1
    for log in zad1_2.read_file(file):
        if i == log_number:
            zad1_2.read_l_logging(log, log_level)
            return
        else:
            i += 1
    print("Invalid log number")

@app.command('task_1_3_1')
def task_1_3_1(file: str, n: int):
    """
    Get random user logs from the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        n (int): The number of logs to analyze.
    """
    zad1_3.print_random_user_logs(file, n)

app.command('task_1_3_2_user')
def task_1_3_2_user(file: str, user: str):
    """
    Get the average log length for a specific user in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        user (str): The user to analyze.
    """
    zad1_3.print_average_log_length(file, user)

@app.command('task_1_3_2_all')
def task_1_3_2_all(file: str):
    """
    Get the average log length for all users in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
    """
    zad1_3.print_average_log_length(file)

@app.command('task_1_3_3')
def task_1_3_3(file: str):
    """
    Get the most and least frequent logging user in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
    """
    zad1_3.print_most_and_least_frequent_logging_user(file)

@app.command('task_1_extra')
def task_1_extra(file: str, max_interval: int, max_attempts: int, single_user: bool):
    """
    Detect brute force attacks in the SSH log file.

    Args:
        file (str): The path to the SSH log file.
        max_interval (int): The maximum interval between logins.
        max_attempts (int): The maximum number of login attempts.
        single_user (bool): Whether to analyze a single user or all users.
    """
    zad1_dodatkowe.detect_bruteforce(file, max_interval, max_attempts, single_user)




if __name__ == "__main__":
    app()