from SSHLogEntryRefactoraized import SSHLogEntry, RejectedPasswordLogEntry, AcceptedPasswordLogEntry, ErrorLogEntry, OtherLogEntry
import ipaddress
from typing import List, Callable, Iterator
from lab5.zad1_1 import get_message_type


class SSHLogJournal:
    entries: List[SSHLogEntry]

    def __init__(self) -> None:
        self.entries = []

    def __len__(self) -> int:
        return len(self.entries)

    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.entries)

    def __contains__(self, item) -> bool:
        return item in self.entries

    def append(self, log_entry: str) -> None:
        item: SSHLogEntry
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

    def filter_by_criteria(self, criteria: Callable[[SSHLogEntry], bool]) -> List[SSHLogEntry]:
        filtered_entries: List[SSHLogEntry] = []
        for entry in self.entries:
            if criteria(entry):
                filtered_entries.append(entry)
        return filtered_entries
    
    def filter_by_ip(self, ip: str) -> List[SSHLogEntry]:
        ip_addr = ipaddress.IPv4Address(ip)
        return self.filter_by_criteria(lambda entry: entry.get_ipv4() == ip_addr)

    def __getattr__(self, item: str) -> List:
        if item == "ip":
            return [entry.get_ipv4() for entry in self.entries]
        elif item == "index":
            return [i for i in range(len(self.entries))]
        elif item == "date":
            return [entry.date for entry in self.entries]
        else:
            raise AttributeError(f"Attribute {item} not found")
