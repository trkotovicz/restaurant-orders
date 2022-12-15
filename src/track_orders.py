class TrackOrders:
    def __init__(self):
        self._data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append(
            {"customer": customer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        frequency = {}

        for order in self._data:
            if order["customer"] == customer:
                if order["order"] not in frequency:
                    frequency[order["order"]] = 1
                else:
                    frequency[order["order"]] += 1

        return max(frequency, key=frequency.get)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
