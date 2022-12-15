class TrackOrders:
    def __init__(self):
        self._data = []
        self._dishes = set()
        self._days = set()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def all_dishes(self):
        for dish in self._data:
            self._dishes.add(dish["order"])

    def open_days(self):
        for day in self._data:
            self._days.add(day["day"])

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
        already_ordered = set()
        self.all_dishes()

        for order in self._data:
            if order["customer"] == customer:
                already_ordered.add(order["order"])

        return self._dishes.difference(already_ordered)

    def get_days_never_visited_per_customer(self, customer):
        self.open_days()
        already_went = set()

        for order in self._data:
            if order["customer"] == customer:
                already_went.add(order["day"])

        return self._days.difference(already_went)

    def get_busiest_day(self):
        busiest_day = {}

        for order in self._data:
            if order["day"] not in busiest_day:
                busiest_day[order["day"]] = 1
            else:
                busiest_day[order["day"]] += 1

        return max(busiest_day, key=busiest_day.get)

    def get_least_busy_day(self):
        lazyest_day = {}

        for order in self._data:
            if order["day"] not in lazyest_day:
                lazyest_day[order["day"]] = 1
            else:
                lazyest_day[order["day"]] += 1

        return min(lazyest_day, key=lazyest_day.get)
