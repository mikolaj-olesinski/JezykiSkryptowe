from read_l import read_l

def entry_to_dict(log: tuple) -> dict:
    return {
        "host": log[0],
        "date": log[1],
        "request": log[2],
        "code": log[3],
        "bytes_sent": log[4]
    }

def log_to_dict(logs: list[tuple]) -> dict:
    log_dict = {}
    for log in logs:
        host = log[0]
        if host in log_dict:
            log_dict[host].append(entry_to_dict(log))
        else:
            log_dict[host] = [entry_to_dict(log)]
    return log_dict

def get_addrs(logs: dict) -> list:
    return list(logs.keys())


def print_dict_entry_dates(logs: dict):
    for key, value in logs.items():
        requests_number = len(value)
        succesful_requests = sum([1 for req in value if req["code"] == 200])
        first_request = min(value, key = lambda x : x["date"]) 
        last_request = max(value, key = lambda x : x["date"]) 
        ratio = succesful_requests / requests_number
        print(
            f"host: {key}, number of requests: {requests_number}, successful/total: {ratio:.2f}, first: {first_request['date']}, last: {last_request['date']} \n"
            )
        
if __name__ == "__main__":
    logs = read_l()
    logs = log_to_dict(logs)
    print_dict_entry_dates(logs)

