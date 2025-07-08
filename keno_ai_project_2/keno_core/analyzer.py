import pandas as pd
from collections import Counter

def get_hot_cold_numbers(draws_df, top_n=10):
    all_numbers = draws_df.values.flatten()
    number_counts = Counter(all_numbers)
    hot = [num for num, _ in number_counts.most_common(top_n)]
    cold = [num for num, _ in number_counts.most_common()[-top_n:]]
    return hot, cold
