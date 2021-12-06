def find_gamma_rate():
    """
    For Part 1
    """
    with open('input.txt', 'r') as reader:

        # each line in the report consists of 12 characters
        # if each line didn't always contain 12 characters, I would have done this differently
        chars = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        try:
            for line in reader:
                split_line = line.strip()
                # thanks to https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
                for idx, bit in enumerate(split_line):
                    # if zeroes are more frequent, then the end value will be negative
                    if int(bit) == 0:
                        chars[idx] -= 1
                    # if ones are more frequent, then the end value will be positive
                    elif int(bit) == 1:
                        chars[idx] += 1
            end_code_list = []
            for char in chars:
                if char > 0:
                    end_code_list.append(1)
                elif char < 0:
                    end_code_list.append(0)

            gamma_rate_binary = "".join([str(int) for int in end_code_list])
            return gamma_rate_binary

        finally:
            reader.close()


def find_epsilon_rate():
    """
    For Part 1
    """
    epsilon_rate = []
    gamma_rate_binary = find_gamma_rate()
    for char in gamma_rate_binary:
        if char == "0":
            epsilon_rate.append(1)
        elif char == "1":
            epsilon_rate.append(0)
    epsilon_rate_binary = "".join([str(int) for int in epsilon_rate])
    return epsilon_rate_binary


def find_power_consumption():
    """
    For Part 1
    """
    # thanks to https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
    gamma_rate = int(find_gamma_rate(), 2)
    epsilon_rate = int(find_epsilon_rate(), 2)
    return gamma_rate * epsilon_rate


def find_most_bits(list_of_ints, bit_index, oxygen):
    """
    Helper Function for Part 2
    """
    count_zeroes = 0
    count_ones = 0
    list_of_zeroes_at_given_index = []
    list_of_ones_at_given_index = []

    if len(list_of_ints) == 1:
        return list_of_ints[0]
    else:
        for idx, num in enumerate(list_of_ints):
            if int(num[bit_index]) == 0:
                list_of_zeroes_at_given_index.append(list_of_ints[idx])
                count_zeroes += 1
            elif int(num[bit_index]) == 1:
                list_of_ones_at_given_index.append(list_of_ints[idx])
                count_ones += 1
        if oxygen == True:
            # for oxygen, return the longer list
            # if the lists are the same length, return the ones list
            if count_zeroes > count_ones:
                return list_of_zeroes_at_given_index
            else:
                return list_of_ones_at_given_index
        elif oxygen == False:
            # for CO2, return the shorter list
            # if the lists are the same length, return the zeroes list
            if count_zeroes > count_ones:
                return list_of_ones_at_given_index
            else:
                return list_of_zeroes_at_given_index


def find_oxygen_generator_rating():
    """
    For Part 2
    """
    with open('input.txt', 'r') as reader:
        try:

            new_list = []
            for line in reader:
                cleaned_line = line.strip()
                new_list.append(cleaned_line)
            bit_index = 0
            while bit_index < 12:
                if len(new_list) == 1:
                    return new_list[0]
                else:
                    filtered_list = find_most_bits(
                        new_list, bit_index, oxygen=True)
                    new_list = filtered_list
                    bit_index += 1

            return new_list[0]

        finally:
            reader.close()


def find_co2_scrubber_rating():
    """
    For Part 2
    """
    with open('input.txt', 'r') as reader:
        try:

            new_list = []
            for line in reader:
                cleaned_line = line.strip()
                new_list.append(cleaned_line)

            bit_index = 0
            while bit_index < 12:
                if len(new_list) == 1:
                    return new_list[0]
                else:
                    filtered_list = find_most_bits(
                        new_list, bit_index, oxygen=False)
                    new_list = filtered_list
                    bit_index += 1

            return new_list[0]

        finally:
            reader.close()


def find_life_support_rating():
    # thanks to https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
    oxygen_rating = int(find_oxygen_generator_rating(), 2)
    co2_rating = int(find_co2_scrubber_rating(), 2)
    return oxygen_rating * co2_rating


# print(find_oxygen_generator_rating())
# print(find_co2_scrubber_rating())
# print(find_life_support_rating())
