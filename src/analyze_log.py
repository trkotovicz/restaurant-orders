import csv


def analyze_log(path_to_file):
    data = read(path_to_file)
    most_ordered_maria = maria_most_ordered(data)
    arnaldo_hamburguer = arnaldo_ordered_hamburguer(data)

    return f"""\
        {most_ordered_maria}
        {arnaldo_hamburguer}"""


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


def maria_most_ordered(data):
    frequency = {}

    for order in data:
        if order["customer"] == 'maria':
            if order["order"] not in frequency:
                frequency[order["order"]] = 1
            else:
                frequency[order["order"]] += 1

    # https://datagy.io/python-get-dictionary-key-with-max-value/
    return max(frequency, key=frequency.get)


def arnaldo_ordered_hamburguer(data):
    count = 0

    for order in data:
        if order["customer"] == 'arnaldo' and order["order"] == 'hamburguer':
            count += 1

    return count


def joao_never_tasted(data):
    ...


def joao_never_went(data):
    ...


if __name__ == "__main__":
    # print(read("data/orders_1.csv"))
    print(analyze_log("data/orders_1.csv"))
