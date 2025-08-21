from use_cases.task_scheduling import RestaurantOrderSimulation


def simulate_restaurant_order_processing():
    menu = ["pizza", "samosa", "pasta", "biryani", "burger"]
    RestaurantOrderSimulation(menu)


if __name__ == "__main__":
    simulate_restaurant_order_processing()
