def find_max(numbers):
    maximum = numbers[0]
    for value in numbers:
        if maximum < value:
            maximum = value
    return maximum