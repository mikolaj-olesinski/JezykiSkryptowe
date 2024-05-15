

# 199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# 199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
# burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0

import sys
import re
from datetime import datetime
from pytz import timezone, country_timezones

#ip, date, req, status_code, size

def read_l(line) -> tuple:

    pattern = r'^(\S+) - - \[([\w:/]+ [+\-]\d{4})\] "(.*?)" (\d{3}) (\d+|-)$'
    date_pattern = "%d/%b/%Y:%H:%M:%S %z"

    match = re.match(pattern, line)
    if match:
        ip, date, req, code, bytes = match.groups()
        date_obj = datetime.strptime(date, date_pattern)
        bytes = bytes if bytes != "-" else None

        method = req.split()[0]
        resource = req.split()[1]
        return (ip, date_obj, method, resource, code, bytes) 
    else:
        return None
    
def filter_logs_by_date(logs, date_from, date_to):
    filtered_logs = []
    for log in logs:
        log_tup = read_l(log)
        log_date = log_tup[1]  
        log_date_str = log_date.strftime("%Y-%m-%d")  
        date_from_str = date_from.strftime("%Y-%m-%d")
        date_to_str = date_to.strftime("%Y-%m-%d")  
        if date_from_str <= log_date_str <= date_to_str:
            filtered_logs.append(log)
    return filtered_logs
    

if __name__ == "__main__":
    logs = read_l('burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0')
    print(logs[0])
    print(logs[1])
    print(logs[2])
    print(logs[3])




