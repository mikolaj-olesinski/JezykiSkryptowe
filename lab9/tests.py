import pytest
from datetime import datetime
from lab5.zad1_1 import read_log, get_message_type
from SSHLogEntryRefactoraized import SSHLogEntry, RejectedPasswordLogEntry, AcceptedPasswordLogEntry, ErrorLogEntry, OtherLogEntry, create_ssh_log_entry
from SSHLogJournalRefactoraized import SSHLogJournal
import ipaddress

test_logs = [
    'Dec 10 07:51:15 LabSZ sshd[24324]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]',
    'Dec 10 07:56:02 LabSZ sshd[24331]: Failed password for invalid user fztu from 52.80.34.196 port 36060 ssh2',
    'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 254.234.31.186 port 38926 ssh2',
    'Dec 10 07:53:26 LabSZ sshd[24329]: Connection closed by 194.190.163.333 [preauth]',
    'Dec 10 07:56:13 LabSZ sshd[24333]: Did not receive identification string from 256.207.3.333', 
    'Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 999.137.62.142 port 49116 ssh2',
    'Dec 10 07:28:25 LabSZ sshd[24265]: Accepted password for user webmaster from 103.207.39.1659',
    'Dec 10 07:55:55 LabSZ sshd[24331]: input_userauth_request: invalid user test [preauth]',
    'Dec 10 07:42:49 LabSZ sshd[24318]: pam_unix(sshd:auth): check pass; user unknown',
    'Dec 10 07:42:49 LabSZ sshd[24318]: input_userauth_request: invalid user inspur [preauth]'
]




expected_dates = [
    datetime(1900, 12, 10, 7, 51, 15),
    datetime(1900, 12, 10, 7, 56, 2),
    datetime(1900, 12, 10, 6, 55, 48),
    datetime(1900, 12, 10, 7, 53, 26),
    datetime(1900, 12, 10, 7, 56, 13),
    datetime(1900, 12, 10, 9, 32, 20),
    datetime(1900, 12, 10, 7, 28, 25),
    datetime(1900, 12, 10, 7, 55, 55),
    datetime(1900, 12, 10, 7, 42, 49),
    datetime(1900, 12, 10, 7, 42, 49)
]

expected_ipaddresses = [
    ipaddress.IPv4Address('195.154.37.122'),
    ipaddress.IPv4Address('52.80.34.196'),
    ipaddress.IPv4Address('254.234.31.186'),
    lambda: ipaddress.IPv4Address('194.190.163.333'),
    lambda: ipaddress.IPv4Address('256.234.31.186'),  
    lambda: ipaddress.IPv4Address('999.137.62.142'),
    None,
    None,
    None,
    None
]

@pytest.mark.parametrize("log, expected_date", zip(test_logs, expected_dates))
def test_sshlog_entry_creation_time(log, expected_date):
    entry: SSHLogEntry = create_ssh_log_entry(log)
    assert entry.date == expected_date


@pytest.mark.parametrize("log, expected_ip", zip(test_logs, expected_ipaddresses))
def test_sshlog_entry_creation_ip(log, expected_ip):
    entry: SSHLogEntry = create_ssh_log_entry(log)
    
    if callable(expected_ip):
        with pytest.raises(ipaddress.AddressValueError):
            entry.get_ipv4()
    else:
        assert entry.get_ipv4() == expected_ip


journal = SSHLogJournal()
@pytest.mark.parametrize(
    "log, expected_type",
    [
        (test_logs[0], ErrorLogEntry),
        (test_logs[1], RejectedPasswordLogEntry),
        (test_logs[2], RejectedPasswordLogEntry),
        (test_logs[3], OtherLogEntry),
        (test_logs[4], OtherLogEntry),
        (test_logs[5], AcceptedPasswordLogEntry),
        (test_logs[6], AcceptedPasswordLogEntry),
        (test_logs[7], OtherLogEntry),
        (test_logs[8], OtherLogEntry),
        (test_logs[9], OtherLogEntry)
    ]
)

def test_sshlog_journal_entry_type(log, expected_type):
    journal.append(log)
    assert isinstance(journal.entries[-1], expected_type)