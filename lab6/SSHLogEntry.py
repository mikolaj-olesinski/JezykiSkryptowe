from abc import ABC, abstractmethod
import re, ipaddress
from datetime import datetime
from lab5.zad1_1 import get_user_from_log, get_ipv4s_from_log, read_log, get_message_type

class SSHLogEntry(ABC):

    def __init__(self, log):
        try:
            log_dict = read_log(log)
            self.date = log_dict[0]
            self.host_name = log_dict[1]
            self.app_name = log_dict[2]
            self.pid = log_dict[3]
            self._message = log_dict[4]
        except:
            raise ValueError("Invalid log format")

    def __str__(self):
        return f"SSHLogEntry(date={self.date}, host_name={self.host_name}, app_name={self.app_name}, pid={self.pid}, message={self._message})"

    def get_ipv4(self):
        ip_adresses = get_ipv4s_from_log(self._message)
        if len(ip_adresses) == 0:
            return None
        else:
            return ipaddress.IPv4Address(ip_adresses[-1])

    
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @property
    def has_ip(self):
        return self.get_ipv4() is not None

    def __repr__(self):
        months = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }

        month = months[self.date.month]
        return f"{month} {self.date.day} {self.date.strftime('%H:%M:%S')} {self.host_name} {self.app_name}[{self.pid}]: {self._message}"

    def __eq__(self, other):
        if not isinstance(other, SSHLogEntry):
            return False
        return self.date == other.date 

    def __lt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object")
        return self.date < other.date

    def __gt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object")
        return self.date > other.date
    
    



class RejectedPasswordLogEntry(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)
        self.user = self.extract_user()
        self.ip = self.get_ipv4()
        self.port = self.extract_port()

    def extract_user(self):
        failed_password_pattern = r'Failed password for (\S+).*'
        user = get_user_from_log(self._message)
        if user is None:
            user = re.search(failed_password_pattern, self._message).group(1) if re.search(failed_password_pattern, self._message) else None
        return user
    
    def extract_port(self):
        port_pattern = r'port (\d+).*'
        port = re.search(port_pattern, self._message).group(1) if re.search(port_pattern, self._message) else None
        return port

    def validate(self):
        return get_message_type(self._message) == 'Failed login' and self.user is not None and self.ip is not None and self.port is not None
    
    def type(self):
        return 'RejectedPasswordLogEntry'


class AcceptedPasswordLogEntry(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)
        self.user = self.extract_user()

    def extract_user(self):
        accepted_password_pattern = r'Accepted password for (\S+).*'
        user = get_user_from_log(self._message)
        if user is None:
            user = re.search(accepted_password_pattern, self._message).group(1) if re.search(accepted_password_pattern, self._message) else None
        return user

    def validate(self):
        return get_message_type(self._message) == 'Accepted password' and self.user is not None
    
    def type(self):
        return 'AcceptedPasswordLogEntry'


class ErrorLogEntry(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)
        self.ip = self.get_ipv4()

    def validate(self):
        return get_message_type(self._message) == 'Error' and self.ip is not None
    
    def type(self):
        return 'ErrorLogEntry'

class OtherLogEntry(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)

    def validate(self):
        return True  
    
    def type(self):
        return 'OtherLogEntry'

