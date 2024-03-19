from getters import *

def count_codes(code):
    counter = 0
    for line in sys.stdin:
        if get_response_code(line) == code:
            counter += 1
    return counter


def sum_data():
    total_data = 0
    for line in sys.stdin:
        data = get_bytes(line)
        if get_request(line) == "GET" and data != "-":
            total_data += int(get_bytes(line))
    return total_data


def biggest_resource():
    max = 0
    path = ""
    for line in sys.stdin:
        bytes = get_bytes(line)
        if bytes.isdigit() and int(bytes) > max:
            max = int(bytes)
            path = get_path(line)
    return (path, max)



def graphics_ratio():
    graphics = 0
    others = 0
    for line in sys.stdin:
        if get_file_extension(line) in ["gif", "jpg", "jpeg", "xbm"]:
            graphics += 1
        else:
            others += 1
    return graphics/others

def to_datetime_object(date):
    date_format = "%d/%b/%Y:%H:%M:%S"
    try:
        date_ob = datetime.strptime(date, date_format)
        return date_ob
    except(ValueError, AttributeError):
        return None

def is_beetwen_hours(start, end, line):
    date = to_datetime_object(get_date(line))
    if (date.hour >= start or date.hour <= end - 1) and (date.hour > 0 and date.hour < 24):
        return True
    return False


def get_day_of_week(line):
    date = to_datetime_object(get_date(line))
    return date.weekday()
