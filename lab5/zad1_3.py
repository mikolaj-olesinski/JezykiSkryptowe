import zad1_1
import random
import numpy as np
import sys
from collections import defaultdict
from datetime import datetime

def print_random_user_logs(file=sys.stdin, n=5):
    logs_from_all_users = defaultdict(list)

    for line in zad1_1.read_file(file):
        log = zad1_1.read_log(line)
        user = zad1_1.get_user_from_log(log[-1])
        logs_from_all_users[user].append(log[-1])
    
    user = random.choice(list(logs_from_all_users.keys()))
    logs_from_user = logs_from_all_users[user]

    if n < 0:
        print("Liczba logów nie może być ujemna.")
        return
    elif len(logs_from_user) < n:
        print(f"Użytkownik {user} ma za mało logów. Znaleziono tylko {len(logs_from_user)}.")
        n = len(logs_from_user)

    selected_logs = random.sample(logs_from_user, n)
    print(f"Losowe {n} logów użytkownika {user}:")
    for log in selected_logs:
        print(log)


def print_most_and_least_frequent_logging_user(file=sys.stdin):
    users = {}
    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        user = zad1_1.get_user_from_log(log[-1])
        if zad1_1.get_message_type(log[-1]) == "Successful login":
            if user in users:
                users[user] += 1
            else:
                users[user] = 1
    
    most_frequent_user = max(users, key=users.get)
    least_frequent_user = min(users, key=users.get)
    print(f"Najczęściej logujący się użytkownik: {most_frequent_user}, liczba logowań: {users[most_frequent_user]}")
    print(f"Najrzadziej logujący się użytkownik: {least_frequent_user}, liczba logowań: {users[least_frequent_user]}")


def print_average_log_length(file=sys.stdin, picked_user=None):
    # Tworzymy słownik, w którym kluczem jest użytkownik, a wartością czas, w którym zalogował się i wylogował
    users_session_starts = defaultdict(list)
    users_session_durations = defaultdict(list)


    for log in zad1_1.read_file(file):
        log = zad1_1.read_log(log)
        user_from_logs = zad1_1.get_user_from_log(log[-1])
        message_type = zad1_1.get_message_type(log[-1])

        if message_type == "Successful login":
            users_session_starts[user_from_logs].append(log[0])
        elif message_type == "Connection closed":
            if users_session_starts[user_from_logs]:
                start_time = users_session_starts[user_from_logs].pop(0)
                logout_time = log[0]

                if logout_time < start_time: #zmiana roku
                    logout_time = logout_time.replace(year=logout_time.year+1)
        
                duration = (logout_time - start_time).total_seconds()
                users_session_durations[user_from_logs].append(duration)
    

                #print(f"Użytkownik {user_from_logs} zalogował się o {start_time} i wylogował o {log[0]}. Sesja trwała {duration:.2f}s")
        
    # for user in users_session_durations:
    #     print(f"Użytkownik {user} srednia długość logów: {np.mean(users_session_durations[user]):.2f}s odchylenie standardowe: {np.std(users_session_durations[user]):.2f}s")
    
    #jeśli wybrano użytkownika, to obliczamy dla niego a jeśli nie, to dla wszystkich
    if picked_user is not None:
        if picked_user not in users_session_durations:
            print(f"Użytkownik {picked_user} nie ma logów typu 'Successful login' ani 'Connection closed' lub nie istnieje")
        else:
            print(f"Średnia długość logów użytkownika {picked_user}: {np.mean(users_session_durations[picked_user]):.2f}s odchylenie standardowe: {np.std(users_session_durations[picked_user]):.2f}s")

    else:
        total_logs = []
        for user, logs in users_session_durations.items():
            for log in logs:
                total_logs.append(log)
        print(f"Średnia długość logów wszystkich użytkowników: {np.mean(total_logs):.2f}s odchylenie standardowe: {np.std(total_logs):.2f}s")


if __name__ == "__main__":
    print_most_and_least_frequent_logging_user()
