import csv
import shutil

def print_dotted_line():
    terminal_width, _ = shutil.get_terminal_size()
    dotted_line = '-' * terminal_width
    print_green(dotted_line)





def save_list_of_dicts_to_csv(data, file_path):
    if not data:
        print_green("No data to save.")
        return

    field_names = data[0].keys()

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

    print_green(f"Data saved to {file_path}.")


def read_csv_to_list_of_dicts(file_path):
    data = []

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

def print_green(text):
    green_text = "\033[32m" + text + "\033[0m"
    print(green_text)
