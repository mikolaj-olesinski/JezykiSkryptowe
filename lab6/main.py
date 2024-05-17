from SSHLogEntry import SSHLogEntry, RejectedPasswordLogEntry, AcceptedPasswordLogEntry, ErrorLogEntry, OtherLogEntry
from SSHLogJournal import SSHLogJournal
from SSHUser import SSHUser
from datetime import datetime
from lab5.zad1_1 import read_file, read_log, get_user

test_logs = ['Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2', 
             'Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2',
             'Dec 10 07:51:15 LabSZ sshd[24324]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]',
             'Dec 10 07:53:26 LabSZ sshd[24329]: Connection closed by 194.190.163.22 [preauth]',
             'Dec 10 07:55:55 LabSZ sshd[24331]: input_userauth_request: invalid user test [preauth]',
             'Dec 10 07:56:02 LabSZ sshd[24331]: Failed password for invalid user !user from 52.80.34.196 port 36060 ssh2'
             'Dec 10 07:56:13 LabSZ sshd[24333]: Did not receive identification string from 103.207.39.165']

def zad1():
    logEntryWithIp = RejectedPasswordLogEntry(test_logs[0])
    logEntryWithoutIP = OtherLogEntry(test_logs[4])
    print("Date: ", logEntryWithIp.date)
    print("Host: ", logEntryWithIp.host_name)
    print("App name: ", logEntryWithIp.app_name)
    print("PID: ", logEntryWithIp.pid)
    print("Message: ", logEntryWithIp._message)
    print()
    print("__str__", logEntryWithIp)
    print()
    print("Log entry with ip:   ", logEntryWithIp.get_ipv4())
    print("Log entry without ip:    ", logEntryWithoutIP.get_ipv4())


def zad2():
    accepted_password_log = AcceptedPasswordLogEntry(test_logs[1])
    rejected_password_log = RejectedPasswordLogEntry(test_logs[0])
    error_log = ErrorLogEntry(test_logs[2])
    other_log = OtherLogEntry(test_logs[3])

    print("Accepted password log:   ", accepted_password_log.type(), "user:", accepted_password_log.user)
    print("Rejected password log: ", rejected_password_log.type(), "user:", rejected_password_log.user, "ip:", rejected_password_log.ip, "port:", rejected_password_log.port)
    print("Error log: ", error_log.type(), "ip:", error_log.ip)
    print("Other log: ", other_log.type())

def zad3():
    accepted_password_log = AcceptedPasswordLogEntry(test_logs[0])
    accepted_password_log2 = AcceptedPasswordLogEntry(test_logs[1])
    
    print("validate for wrong accepted password log: ", accepted_password_log.validate())
    print("validate for correct accepted password log: ", accepted_password_log2.validate())

def zad5():
    log_with_ip = RejectedPasswordLogEntry(test_logs[0])
    log_without_ip = OtherLogEntry(test_logs[4])
    print("Log with ip: ", log_with_ip.has_ip)
    print("Log without ip: ", log_without_ip.has_ip)

def zad6():
    #'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2', 
    #'Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2',
    log = RejectedPasswordLogEntry(test_logs[0])
    print("__repr__", repr(log))

    log2 = AcceptedPasswordLogEntry(test_logs[1])
    
    #patrzymy na date
    print("__eq__", log == log2)
    print("__lt__", log < log2)
    print("__gt__", log > log2)


def zad7(show_users=False):
    entrys_and_users = []
    journal = SSHLogJournal()
    iter_journal = iter(journal)
    usernames = ['root', '', '!abc', '1dasd', 'cs da', "fdsfuhjsdiufhisudhfuihfuhsduyfufsduyfbuydfuysbhfuhsdbfuhdsbuhfbdsufbsdjfbdsuhbfuhdsbfuhdsbfusbfubdsudfbsudbfdsbu"]

    for user, log in zip(usernames, test_logs):
        user = SSHUser(user)

        journal.append(log)
        log_j = next(iter_journal)

        log_dict = read_log(log)
        user_from_log = get_user(log_dict[-1])
        user_from_log = SSHUser(user_from_log, log_dict[0])

        entrys_and_users.append(user)
        entrys_and_users.append(log_j)
        entrys_and_users.append(user_from_log)

    
    for entry in entrys_and_users:
        print(entry.validate())


        if isinstance(entry, SSHUser) and show_users:
            print("user before", entry.username)

                

def test_journal():
    journal = SSHLogJournal()
    for log in test_logs:
        journal.append(log)

    print("__len__", len(journal))
    print()
    iter_journal = iter(journal)
    print("__iter__", iter_journal)
    print("next iter", repr(next(iter_journal)))
    print("next iter", repr(next(iter_journal)))
    print()
    log = AcceptedPasswordLogEntry(test_logs[1])
    print("__contains__", log in journal)
    print("__contains__", "aa" in journal)

    print()
    print("filter by ip: 173.234.31.186", journal.filter_by_ip("173.234.31.186"))

    print()
    date1 = datetime.strptime("Dec 10 07:51:00", '%b %d %H:%M:%S')
    date2 = datetime.strptime("Dec 10 07:54:00", '%b %d %H:%M:%S')
    print("filter by date: ", journal.filter_by_criteria(lambda entry: date1 <= entry.date <= date2))

    print()
    print("__getattr__")
    print(journal.ip[:5])
    print(journal.index[:5])
    print(journal.date[:5])
        
if __name__ == '__main__':
    print("---------------------------------------- Zadanie 1 ----------------------------------------")
    zad1()

    print("\n\n\n---------------------------------------- Zadanie 2 ----------------------------------------")
    zad2()

    print("\n\n\n---------------------------------------- Zadanie 3 ----------------------------------------")
    zad3()

    print("\n\n\n---------------------------------------- Zadanie 5 ----------------------------------------")
    zad5()

    print("\n\n\n---------------------------------------- Zadanie 6 ----------------------------------------")
    zad6()

    print("\n\n\n---------------------------------------- Zadanie 7 ----------------------------------------")
    zad7(show_users=True)

    print("\n\n\n----------------------------------------  Test Journal ----------------------------------------")
    test_journal()
