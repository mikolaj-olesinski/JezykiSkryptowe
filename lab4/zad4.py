import subprocess
import os

def analyze_files(directory):
    results = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
               
                result = subprocess.run(["java", "zad4", filepath], capture_output=True, text=True)
                result_stdout = result.stdout.strip()  
                if result.returncode == 0 and result_stdout:  
                    result_dict = parse_json(result_stdout)  
                    results.append(result_dict)
            except subprocess.CalledProcessError:
                print(f"Błąd podczas analizowania pliku {filepath}")

    return results

def parse_json(json_string):
    result_dict = {}
    for line in json_string.split("\n"):
        if ":" in line:
            key, value = line.split(": ", 1) 
            result_dict[key.strip()] = value.strip().replace(",", "")  
    return result_dict

def print_results(results):
    files_read = len(results)
    sum_chars = 0
    sum_words = 0
    sum_lines = 0
    word_frequency = {}
    char_frequency = {}

    for result in results:
        sum_chars += int(result.get('"charCount"', "0"))
        sum_words += int(result.get('"wordCount"', "0"))
        sum_lines += int(result.get('"lineCount"', "0"))

        most_freq_word_in_result = result.get('"mostFrequentWord"', "")
        most_freq_char_in_result = result.get('"mostFrequentChar"', "")

        if most_freq_word_in_result in word_frequency:
            word_frequency[most_freq_word_in_result] += 1
        else:
            word_frequency[most_freq_word_in_result] = 1
        
        if most_freq_char_in_result in char_frequency:
            char_frequency[most_freq_char_in_result] += 1
        else:
            char_frequency[most_freq_char_in_result] = 1

        


    print("Liczba przeczytanych plików:", files_read)
    print("Sumaryczna liczba znaków:", sum_chars)
    print("Sumaryczna liczba słów:", sum_words)
    print("Sumaryczna liczba wierszy:", sum_lines)
    print("Najczęściej występujące słowo:", max(word_frequency, key=word_frequency.get))
    print("Najczęściej występujący znak:", max(char_frequency, key=char_frequency.get))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Złe argumenty wpisane")
        sys.exit(1)

    directory = sys.argv[1]
    results = analyze_files(directory)
    print_results(results)
