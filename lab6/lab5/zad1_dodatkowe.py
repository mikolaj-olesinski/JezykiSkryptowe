import zad1_1
import sys
import re
from collections import defaultdict
from datetime import datetime

def detect_bruteforce(file=sys.stdin, max_interval=100, max_attempts=4, single_user=False):

    if max_interval < 0 or max_attempts < 0:
        print("Parametry max_interval oraz max_attempts nie mogą być ujemne.")
        return

    failed_password_pattern = r'Failed password for (\S+).*'
    repeat_pattern = r'message repeated (\S+) times:'
    ip_attempts = defaultdict(list)

    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        ip = zad1_1.get_ipv4s_from_log(log[-1])

        user = zad1_1.get_user_from_log(log[-1])
        # Jeśli nie udało się znaleźć użytkownika, to sprawdzamy, czy nie jest to próba ataku na roota lub innego użytkownika
        if user is None:
            user = re.search(failed_password_pattern, log[-1]).group(1) if re.search(failed_password_pattern, log[-1]) else None

        if re.search(failed_password_pattern, log[-1]):
            #Dostosowanie klucza do przechowywania prób ataku
            key = ip[-1] if not single_user else str(ip[-1] + " " + user)
            ip_attempts[key].append(log[0])

            # Sprawdzamy, czy w logu jest informacja o wielokrotnym powtórzeniu
            if re.search(repeat_pattern, log[-1]):
                times = re.search(repeat_pattern, log[-1]).group(1)
                for _ in range(int(times) - 1):
                    ip_attempts[key].append(log[0])


            if len(ip_attempts[key]) >= max_attempts:
                time_diff = (ip_attempts[key][-1] - ip_attempts[key][0]).total_seconds()

                if time_diff <= max_interval:
                    if not single_user:
                        print(f"Znaleziono próbę ataku bruteforce z adresu IP {ip}, początek ataku: {ip_attempts[key][0]}, koniec ataku: {ip_attempts[key][-1]}")
                    else:
                        print(f"Znaleziono próbę ataku bruteforce z adresu IP {ip} oraz użytkownika {user}, początek ataku: {ip_attempts[key][0]}, koniec ataku: {ip_attempts[key][-1]}")
                    
                    ip_attempts[key] = []
                else:
                    ip_attempts[key] = ip_attempts[key][1:]


if __name__ == "__main__":
    detect_bruteforce(max_interval=100, max_attempts=10, single_user=True)


