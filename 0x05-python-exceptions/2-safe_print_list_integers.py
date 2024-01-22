def safe_print_list_integers(my_list=[], x=0):
    valid_count = 0
    formatted_values = ""

    for i in range(x):
        try:
            formatted_values += "{:d}".format(my_list[i])
            valid_count += 1
        except (ValueError, TypeError, IndexError):
            print("IndexError occurred at i =", i)
            continue

    print(formatted_values)
    return valid_count
