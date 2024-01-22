#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            div = 0
        except ZeroDivisionError:
            print("Division by 0")
            div = 0
        except IndexError:
            print("Out of range")
            div = 0
        finally:
            result_list.append(div)
    return result_list
