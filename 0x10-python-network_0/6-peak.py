def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not isinstance(list_of_integers, list):
        return None

    if not list_of_integers:
        return None

    # Check for peaks
    for i in range(len(list_of_integers)):
        if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
        elif i == len(list_of_integers) - 1 and list_of_integers[i] >= list_of_integers[i - 1]:
            return list_of_integers[i]
        elif list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

    return None
