from read_l import read_l

def sort_log(logs: list[tuple], sort_by: int) -> list[tuple]:
    try:
        sorted_logs = sorted((log for log in logs if log[sort_by] is not None), key=lambda x: x[sort_by])
        return sorted_logs
    except IndexError:
        print("Podano niepoprawny numer elementu krotki do sortowania.")
        return logs
    
def get_entries_addr(logs: list[tuple], address: str) -> list[tuple]:
    return list(filter(lambda log: log[0] == address or log[0].split(".")[-1] == address, logs))


def get_reads(logs: list[tuple], status_code: str) -> list[tuple]:
    return list(filter(lambda log: log[3] == int(status_code), logs))

def get_entries_by_extension(logs: list[tuple], extension: str) -> list[tuple]:
    return list(filter(lambda log: log[2].endswith("." + extension), logs))


def print_entries(logs: list[tuple], start: int):
    for log in logs[start:]:
        print(log)


if __name__ == "__main__":
    logs = read_l()
    
    logs = sort_log(logs, 3124121)
    print_entries(logs, 10000000)