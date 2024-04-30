import argparse
import zad1_1
import zad1_2
import zad1_3

def main():
    parser = argparse.ArgumentParser(description="CLI for log analysis")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_task_1_1_1 = subparsers.add_parser("task_1_1_1", help="Path log file to dict")
    parser_task_1_1_1.add_argument("file", help="Path to the log file")
    parser_task_1_1_1.add_argument("log_number", type=int, help="Number of log to analyze")

    parser_task_1_1_2 = subparsers.add_parser("task_1_1_2", help="Get IPv4 addresses from log")
    parser_task_1_1_2.add_argument("file", help="Path to the log file")
    parser_task_1_1_2.add_argument("log_number", type=int, help="Number of log to analyze")

    parser_task_1_1_3 = subparsers.add_parser("task_1_1_3", help="Get user from log")
    parser_task_1_1_3.add_argument("file", help="Path to the log file")
    parser_task_1_1_3.add_argument("log_number", type=int, help="Number of log to analyze")

    parser_task_1_1_4 = subparsers.add_parser("task_1_1_4", help="Get message type from log")
    parser_task_1_1_4.add_argument("file", help="Path to the log file")
    parser_task_1_1_4.add_argument("log_number", type=int, help="Number of log to analyze")

    parser_task_1_2 = subparsers.add_parser("task_1_2", help="get logger type")
    parser_task_1_2.add_argument("file", help="Path to the log file")
    parser_task_1_2.add_argument("log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Minimum logging level")
    parser_task_1_2.add_argument("log_number", type=int, help="Number of log to analyze")

    parser_task_1_3_1 = subparsers.add_parser("task_1_3_1", help="Get random user logs")
    parser_task_1_3_1.add_argument("file", help="Path to the log file")
    parser_task_1_3_1.add_argument("n", type=int, help="Number of logs to analyze")

    parser_task_1_3_2_user = subparsers.add_parser("task_1_3_2_user", help="Get average log length for user")
    parser_task_1_3_2_user.add_argument("file", help="Path to the log file")
    parser_task_1_3_2_user.add_argument("user", help="User to analyze")

    parser_task_1_3_2_all = subparsers.add_parser("task_1_3_2_all", help="Get average log length for all users")
    parser_task_1_3_2_all.add_argument("file", help="Path to the log file")

    parser_task_1_3_3 = subparsers.add_parser("task_1_3_3", help="Get most and least frequent logging user")
    parser_task_1_3_3.add_argument("file", help="Path to the log file")


    args = parser.parse_args()

    if args.command == "task_1_1_1":
        task_1_1_1(args.file, args.log_number)
    elif args.command == "task_1_1_2":
        task_1_1_2(args.file, args.log_number)
    elif args.command == "task_1_1_3":
        task_1_1_3(args.file, args.log_number)
    elif args.command == "task_1_1_4":
        task_1_1_4(args.file, args.log_number)

    elif args.command == "task_1_2":
        task_1_2(args.file, args.log_level, args.log_number)
    elif args.command == "task_1_3_1":
        task_1_3_1(args.file, args.n)
    elif args.command == "task_1_3_2_user":
        task_1_3_2_user(args.file, args.user)
    elif args.command == "task_1_3_2_all":
        task_1_3_2_all(args.file)
    elif args.command == "task_1_3_3":
        task_1_3_3(args.file)
    else:
        print("Invalid command")
    



def task_1_1_1(file, log_number):
    i = 1

    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(log)
            return
        else:
            i += 1
    
    print("Invalid log number")
    

def task_1_1_2(file, log_number):
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_ipv4s_from_log(log[-1]))
            return
        else:
            i += 1

    print("Invalid log number")


def task_1_1_3(file, log_number):
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_user_from_log(log[-1]))
            return
        else:
            i += 1

    print("Invalid log number")

def task_1_1_4(file, log_number):
    i = 1
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        if i == log_number:
            print(zad1_1.get_message_type(log[-1]))
            return
        else:
            i += 1

    print("Invalid log number")

def task_1_2(file, log_level, log_number):
    i = 1
    for log in zad1_2.read_file(file):
        if i == log_number:
            zad1_2.read_l_logging(log, log_level)
            return
        else:
            i += 1

    print("Invalid log number")


def task_1_3_1(file, n):
    zad1_3.print_random_user_logs(file, n)

def task_1_3_2_user(file, user):
    zad1_3.print_average_log_length(file, user)

def task_1_3_2_all(file):
    zad1_3.print_average_log_length(file)

def task_1_3_3(file):
    zad1_3.print_most_and_least_frequent_logging_user(file)



if __name__ == "__main__":
    main()
