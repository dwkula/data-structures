# Binary search - iteration

def binary_search(numbers_list, number):
    right_index = len(numbers_list) - 1
    left_index = 0

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2

        if number == numbers_list[mid_index]:
            return mid_index

        if number < numbers_list[mid_index]:
            right_index = mid_index - 1

        if number > numbers_list[mid_index]:
            left_index = mid_index + 1

    return -1


# Binary search - recursive

def binary_search_r(numbers_list, number, left_index, right_index):

    mid_index = (left_index + right_index) // 2

    if number == numbers_list[mid_index]:
        return mid_index

    if number < numbers_list[mid_index]:
        right_index = mid_index - 1

    if number > numbers_list[mid_index]:
        left_index = mid_index + 1

    return binary_search_r(numbers_list, number, left_index, right_index)

# Bubble sort


def bubble_sort(elements, key):
    size = len(elements)

    for k in range(size - 1):
        swapped = False
        for i in range(size - 1 - k):
            if elements[i][key] > elements[i+1][key]:
                tmp = elements[i][key]
                elements[i][key] = elements[i + 1][key]
                elements[i+1][key] = tmp
                swapped = True
            if not swapped:
                break

    return elements


elements = [
    {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]

# Quick sort Hoare


def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:

        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index - 1)
        quick_sort(elements, partition_index + 1, end)


# Quick sort Lomuto


elements = [11, 5, 9, 23, 25, 3, 1, 2, 19]
quick_sort(elements, 0, len(elements) - 1)
print(elements)
