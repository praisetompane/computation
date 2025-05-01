def search(list, value):
    midpoint = 1
    while midpoint > 0:
        midpoint = int(len(list) / 2)
        midpoint_value = list[midpoint]
        if midpoint_value == value:
            return midpoint_value
        elif value <= midpoint_value:
            list = list[0:midpoint]
        else:
            list = list[midpoint:]
    return None


def binary_search(value, arr):
    lowerBound = 0
    length = len(arr)
    upperBound = length - 1

    while lowerBound <= upperBound:
        midpoint = (lowerBound + upperBound) // 2
        if value < arr[midpoint]:
            upperBound = midpoint - 1
        elif value > arr[midpoint]:
            lowerBound = midpoint + 1
        elif value == arr[midpoint]:
            return midpoint
    return None


def binary_search_recursive(value, arr):
    def recurse(upperBound, lowerBound):
        midpoint = (lowerBound + upperBound) // 2
        if value < arr[midpoint]:
            return recurse(lowerBound, midpoint - 1)
        elif value > arr[midpoint]:
            return recurse(midpoint + 1, upperBound)
        elif value == arr[midpoint]:
            return midpoint
        return None

    return recurse(0, len(arr) - 1)


numbers = [1, 2, 4, 5, 6, 8, 8, 9]
print(search(numbers, 9))  # 9
print(search(numbers, 4))  # 4
print(search(numbers, 0))  # 4

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(data, 8))
print(binary_search(8, data))
print(binary_search_recursive(8, data))
