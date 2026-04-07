#input is list of integers
#output is return the first duplicate element and
#if no element is duplicate return -1
def duplicateElement(numbers: list) -> int:
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1

numbers =[4,2,7,6,9,9]
print(duplicateElement(numbers))






