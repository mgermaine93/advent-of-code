def return_product_of_distance_and_depth():
    """
    For Part 1
    """
    with open('input.txt', 'r') as reader:
        horizontal_distance = 0
        vertical_distance = 0
        try:
            for line in reader:
                # thanks to https://stackoverflow.com/questions/40663603/skipping-whitespaces-when-reading-file-python
                split_line = line.strip().split(" ")
                direction = split_line[0]
                distance = int(split_line[1])

                if direction == "forward":
                    horizontal_distance += distance
                elif direction.lower() == "up":
                    vertical_distance -= distance
                elif direction.lower() == "down":
                    vertical_distance += distance

            return horizontal_distance * vertical_distance

        finally:
            reader.close()


def return_product_of_distance_and_depth_including_aim():
    """
    For Part 2
    """
    with open('input.txt', 'r') as reader:
        horizontal_distance = 0
        depth = 0
        aim = 0
        try:
            for line in reader:
                # thanks to https://stackoverflow.com/questions/40663603/skipping-whitespaces-when-reading-file-python
                split_line = line.strip().split(" ")
                direction = split_line[0]
                distance = int(split_line[1])

                if direction == "forward":
                    # forward X does two things:
                    # It increases your horizontal position by X units.
                    # It increases your depth by your aim multiplied by X.
                    horizontal_distance += distance
                    depth += (aim * distance)
                elif direction.lower() == "up":
                    # up X decreases your aim by X units.
                    aim -= distance
                elif direction.lower() == "down":
                    # down X increases your aim by X units.
                    aim += distance

            return horizontal_distance * depth

        finally:
            reader.close()


# print(return_product_of_distance_and_depth())
# print(return_product_of_distance_and_depth_including_aim())
