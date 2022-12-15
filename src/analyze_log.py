import csv


def read(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise ValueError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, 'r') as file:
            file_reader = csv.DictReader(file, ["customer", "order", "day"])
            orders = [row for row in file_reader]
            return orders
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    raise NotImplementedError


if __name__ == "__main__":
    print(read("data/orders_1.csv"))
    # print(analyze_log("data/orders_1.csv"))
