def quick_sort(numbers: list) -> list:
    if len(numbers) <=1:
        return numbers
    index = 1
    pivot = numbers[0]
    less_pivot = []
    equal_topivot =[pivot]
    greater_pivot =[]
    while index < len(numbers):
        if numbers[index] < pivot:
            less_pivot.append(numbers[index])
        elif numbers[index] == pivot:
            equal_topivot.append(numbers[index])
        else:
            greater_pivot.append(numbers[index])
        index +=1
    sorted_less =quick_sort(less_pivot)
    sorted_great = quick_sort(greater_pivot)
    return sorted_less+equal_topivot+sorted_great



numbers =[35,23,67,12,35,45,78,90]
print(quick_sort(numbers))
