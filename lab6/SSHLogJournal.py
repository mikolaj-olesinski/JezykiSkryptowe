from SSHLogEntry import SSHLogEntry, RejectedPasswordLogEntry, AcceptedPasswordLogEntry, ErrorLogEntry, OtherLogEntry
from lab5.zad1_1 import get_message_type
import ipaddress

class SSHLogJournal:
    entries: list[SSHLogEntry]

    def __init__(self):
        self.entries = []

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __contains__(self, item):
        return item in self.entries

    def append(self, log_entry):
        if get_message_type(log_entry) == "Failed login":
            item = RejectedPasswordLogEntry(log_entry)
        elif get_message_type(log_entry) == "Accepted password":
            item = AcceptedPasswordLogEntry(log_entry)
        elif get_message_type(log_entry) == "Error":
            item = ErrorLogEntry(log_entry)
        else:
            item = OtherLogEntry(log_entry)

        if item.validate():
            self.entries.append(item)
        else:
            print(f"Invalid log entry: {log_entry}")


    def filter_by_criteria(self, criteria):
        filtered_entries = []
        for entry in self.entries:
            if criteria(entry):
                filtered_entries.append(entry)
        return filtered_entries
    
    def filter_by_ip(self, ip):
        ip = ipaddress.IPv4Address(ip)
        return self.filter_by_criteria(lambda entry: entry.get_ipv4() == ip)
    

    def __getattr__(self, item):
        if item == "ip":
            return [entry.get_ipv4() for entry in self.entries]
        elif item == "index":
            return [i for i in range(len(self.entries))]
        elif item == "date":
            return [entry.date for entry in self.entries]
        else:
            raise AttributeError(f"Attribute {item} not found")

