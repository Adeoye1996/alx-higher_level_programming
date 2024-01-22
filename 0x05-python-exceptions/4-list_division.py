#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            temp_result = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            temp_result = 0
            print("Wrong type, division by 0, or out of range")
        finally:
            result_list.append(temp_result)

    return result_list
