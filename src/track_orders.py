from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_list = []
        for log in self.orders:
            if log[0] == costumer:
                client_list.append(log[1])
        return Counter(client_list).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        food_list = set()
        food_client = set()
        for food in self.orders:
            food_list.add(food[1])
            if food[0] == costumer:
                food_client.add(food[1])
        return food_list - food_client

    def get_days_never_visited_per_costumer(self, costumer):
        days_list = set()
        days_client = set()
        for day in self.orders:
            days_list.add(day[2])
            if day[0] == costumer:
                days_client.add(day[2])
        return days_list - days_client

    def get_busiest_day(self):
        day_list = []
        for day in self.orders:
            day_list.append(day[2])
        return Counter(day_list).most_common(1)[0][0]

    def get_least_busy_day(self):
        day_list = []
        for day in self.orders:
            day_list.append(day[2])
        return Counter(day_list).most_common()[-1][0]
