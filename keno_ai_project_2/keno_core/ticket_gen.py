import random

def generate_ticket(num_spots=10):
    return sorted(random.sample(range(1, 81), num_spots))
