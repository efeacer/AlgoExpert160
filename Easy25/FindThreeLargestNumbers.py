def findThreeLargestNumbers(array):
    """
    One pass: O(n)
    """
    first_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')
    for item in array:
        if item >= first_max:
            third_max = second_max
            second_max = first_max
            first_max = item
        elif item >= second_max:
            third_max = second_max
            second_max = item
        elif item >= third_max:
            third_max = item
    return [third_max, second_max, first_max]