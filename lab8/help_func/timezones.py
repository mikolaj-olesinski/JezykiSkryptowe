def get_region_from_timezone(timezone):
    file = open("/Users/mikolajolesinski/Desktop/JS/lab8/help_func/timezones_and_regions.txt", "r")
    for line in file:
        if timezone in line:
            return line[6:].strip()