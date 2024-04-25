from statistics import mean


# Assumptions: assumes list is ordered oldest to newest. Assumes validation of values is handled elsewhere
def slidingAlgorithm(input_list, n_val):
    if n_val > len(input_list):
        start_idx = 0
    else:
        start_idx = len(input_list) - n_val
    shortened_list = input_list[start_idx:]
    result = mean(shortened_list)
    return result
