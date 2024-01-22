def safe_print_list_integers(my_list=[], x=0):
    count = 0
    formatted_values = ""

    for i in range(min(x, len(my_list))):
        try:
            formatted_values += "{:d}".format(my_list[i])
            count += 1
        except (ValueError, TypeError):
            pass

    print(formatted_values)
    return count
