from input import INPUT


def find_count_of_slide_window_increases(INPUT):
    """
    For Part 2
    """
    count = 0
    index = 0
    while index + 3 < len(INPUT):
        first_group = INPUT[index] + INPUT[index + 1] + INPUT[index + 2]
        second_group = INPUT[index + 1] + INPUT[index + 2] + INPUT[index + 3]
        if second_group > first_group:
            count += 1
        index += 1
    return count


def find_count_measurement_increases(input=INPUT):
    """
    For Part 1
    """
    count = 0
    index = 1
    while index < len(INPUT):
        if input[index] > input[index - 1]:
            count += 1
        index += 1
    return count


# print(find_count_measurement_increases(INPUT))
# print(find_count_of_slide_window_increases(INPUT))
