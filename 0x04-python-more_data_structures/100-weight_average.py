def weight_average(my_list=[]):
    """Calculate the weighted average of a list of tuples."""
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for tup in my_list:
        total_weighted_sum += tup[0] * tup[1]
        total_weight += tup[1]

    if total_weight != 0:
        return float(total_weighted_sum / total_weight)
    else:
        return 0
