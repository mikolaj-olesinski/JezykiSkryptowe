from getters import *

def count_codes(code, file=sys.stdin):
    counter = 0
    for line in file:
        if get_response_code(line) == code:
            counter += 1
    return counter


def sum_data(file=sys.stdin):
    total_data = 0
    for line in file:
        data = get_bytes(line)
        if data != "-":
            total_data += int(get_bytes(line))
    return total_data


def biggest_resource(file=sys.stdin):
    max = 0
    path = ""
    for line in file:
        bytes = get_bytes(line)
        if bytes.isdigit() and int(bytes) > max:
            max = int(bytes)
            path = get_path(line)
    return (path, max)



def graphics_ratio(file=sys.stdin):
    graphics = 0
    others = 0
    for line in file:
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

    if (start < 0 or start > 23 or end < 0 or end > 23):
        raise ValueError("Wrong hour")
    
    elif (date.hour >= start and date.hour < end):
        return True
    return False


def get_day_of_week(line):
    date = to_datetime_object(get_date(line))
    
    return date.weekday()
