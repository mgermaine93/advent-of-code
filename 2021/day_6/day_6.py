class School:
    def __init__(self, school):
        self.school = school

    def one_day_passes(self):
        count = 0
        for idx, fish in enumerate(self.school):
            if fish != 0:
                self.school[idx] -= 1
            else:
                count += 1
                self.school[idx] = 6
        if count > 0:
            for new_fish in range(count):
                self.new_fish()

    def new_fish(self):
        self.school.append(8)


def get_fish_ages_list():
    """
    Turns the .txt file into a list of ints
    """
    try:
        with open("input.txt", "r") as reader:
            fish_list = reader.read().split(",")
            fish_ages = [int(age) for age in fish_list]
            return fish_ages
    finally:
        reader.close()


def main_function():
    lantern_fish_list = School(get_fish_ages_list())
    for day in range(80):
        lantern_fish_list.one_day_passes()
    return len(lantern_fish_list.school)


# print(main_function())
