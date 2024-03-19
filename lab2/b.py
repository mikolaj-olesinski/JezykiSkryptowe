from helpers import sum_data
import sys

def summed_sent_data():
    summed_sent_data_in_gb = sum_data() / (1024 * 1024 * 1024)
    output = f"Total data sent in GB {summed_sent_data_in_gb:.2f} \n"
    sys.stdout.write(output)


if __name__ == "__main__":
    summed_sent_data()