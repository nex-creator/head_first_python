def selection_sort(my_list: list) -> list:
    n = len(my_list)
    for current_index in range(n):
        min_index = current_index

        # scan the unsorted portion
        for i in range(current_index + 1, n):
            if my_list[i] < my_list[min_index]:
                min_index = i

        # swap only if the minimum is not already at current_index
        if min_index != current_index:
            my_list[current_index], my_list[min_index] = my_list[min_index], my_list[current_index]

    return my_list

my_list  = [23,67,44,11,34,76]
print(selection_sort(my_list))