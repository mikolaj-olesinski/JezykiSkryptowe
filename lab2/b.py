from helpers import sum_data
import sys

def summed_sent_data(file=sys.stdin):
    summed_sent_data_in_gb = sum_data(file) / (1024 * 1024 * 1024)
    output = f"Sumaryczna wyslana liczba danych wynosi: {summed_sent_data_in_gb:.2f} GB \n\n\n"
    return output


if __name__ == "__main__":
    sys.stdout.write(summed_sent_data())

