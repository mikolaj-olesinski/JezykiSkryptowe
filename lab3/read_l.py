

# 199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# 199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
# burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0

import sys
import re
from datetime import datetime

#ip, date, req, status_code, size

def read_l(file=sys.stdin) -> list[tuple]:

    pattern = r'^(\S+) - - \[([\w:/]+ [+\-]\d{4})\] "(.*?)" (\d{3}) (\d+|-)$'
    date_pattern = "%d/%b/%Y:%H:%M:%S %z"
    lines = []
    for line in file:
        match = re.match(pattern, line)
        if match:
            ip, date, req, code, bytes = match.groups()
            date_obj = datetime.strptime(date, date_pattern)
            bytes = int(bytes) if bytes != "-" else None
            lines.append( (ip, date_obj, req, int(code), bytes) )
    return lines
if __name__ == "__main__":
    logs = read_l()
    print(logs[0])
    print(logs[1])
    print(logs[2])
    print(logs[3])