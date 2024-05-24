from abc import ABC, abstractmethod
import re, ipaddress
from datetime import datetime
from typing import Optional
from lab5.zad1_1 import get_user_from_log, get_ipv4s_from_log, read_log, get_message_type

class SSHLogEntry():
    date: datetime
    host_name: str
    app_name: str
    pid : int
    _message: str

    def __init__(self, log) -> None: 
        log_dict = read_log(log)
        if log_dict:
            self.date = log_dict[0]
            self.host_name = log_dict[1]
            self.app_name = log_dict[2]
            self.pid = log_dict[3]
            self._message = log_dict[4]
        else:
            raise ValueError("Invalid log format")

    def __str__(self) -> str:
        return f"SSHLogEntry(date={self.date}, host_name={self.host_name}, app_name={self.app_name}, pid={self.pid}, message={self._message})"

    def get_ipv4(self) -> Optional[ipaddress.IPv4Address]:
        ip_adresses: list[str] = get_ipv4s_from_log(self._message)

        if len(ip_adresses) == 0:
            return None
        else:
            return ipaddress.IPv4Address(ip_adresses[-1])

    
    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def type(self) -> str:
        pass

    @property
    def has_ip(self) -> bool:
        return self.get_ipv4() is not None

    def __repr__(self) -> str:
        months: dict[int, str] = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }

        month: str = months[self.date.month]
        return f"{month} {self.date.day} {self.date.strftime('%H:%M:%S')} {self.host_name} {self.app_name}[{self.pid}]: {self._message}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            return False
        return (self.date, self.host_name, self.app_name, self.pid, self._message) == (other.date, other.host_name, other.app_name, other.pid, other._message)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object")
        return self.date < other.date

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object")
        return self.date > other.date
    
    



class RejectedPasswordLogEntry(SSHLogEntry):
    user: Optional[str]
    ip: Optional[ipaddress.IPv4Address]
    port: Optional[int]

    def __init__(self, log: str) -> None:
        super().__init__(log)
        self.user = self.extract_user()
        self.ip = self.get_ipv4()
        self.port = self.extract_port()

    def extract_user(self) -> Optional[str]:
        failed_password_pattern: str = r'Failed password for (\S+).*'
        user: Optional[str] = get_user_from_log(self._message)
        if user is None:
            match: Optional[re.Match] = re.search(failed_password_pattern, self._message)
            user = match.group(1) if match else None
        return user

    def extract_port(self) -> Optional[int]:
        port_pattern = r'port (\d+).*'
        match: Optional[re.Match] = re.search(port_pattern, self._message)
        return int(match.group(1)) if match else None

    def validate(self) -> bool:
        return (get_message_type(self._message) == 'Failed login' and 
                self.user is not None and 
                self.ip is not None and 
                self.port is not None)

    def type(self) -> str:
        return 'RejectedPasswordLogEntry'


class AcceptedPasswordLogEntry(SSHLogEntry):
    user: Optional[str]

    def __init__(self, log: str) -> None:
        super().__init__(log)
        self.user = self.extract_user()

    def extract_user(self) -> Optional[str]:
        accepted_password_pattern: str = r'Accepted password for (\S+).*'
        user: Optional[str] = get_user_from_log(self._message)
        if user is None:
            match: Optional[re.Match] = re.search(accepted_password_pattern, self._message)
            user = match.group(1) if match else None
        return user

    def validate(self) -> bool:
        return get_message_type(self._message) == 'Accepted password' and self.user is not None

    def type(self) -> str:
        return 'AcceptedPasswordLogEntry'

class ErrorLogEntry(SSHLogEntry):
    ip: Optional[ipaddress.IPv4Address]

    def __init__(self, log) -> None:
        super().__init__(log)
        self.ip = self.get_ipv4()

    def validate(self) -> bool:
        return get_message_type(self._message) == 'Error' and self.ip is not None
    
    def type(self) -> str:
        return 'ErrorLogEntry'

class OtherLogEntry(SSHLogEntry):

    def __init__(self, log) -> None:
        super().__init__(log)

    def validate(self) -> bool:
        return True  
    
    def type(self) -> str:
        return 'OtherLogEntry'



def create_ssh_log_entry(log: str) -> SSHLogEntry:
    if get_message_type(log) == 'Failed login':
        return RejectedPasswordLogEntry(log)
    elif get_message_type(log) == 'Accepted password':
        return AcceptedPasswordLogEntry(log)
    elif get_message_type(log) == 'Error':
        return ErrorLogEntry(log)
    else:
        return OtherLogEntry(log)