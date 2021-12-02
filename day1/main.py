import numpy as np


def main():
    # input file
    file = open('day1/input.csv', 'r')
    val_list = []
    for i in file:
        val_list.append(int(i))

    # part 1
    true_count = 0
    comp_val = val_list[0]
    index = 1
    while index < len(val_list):
        if (val_list[index] - comp_val) > 0:
            true_count += 1
        comp_val = val_list[index]
        index += 1
    print(true_count)

    # part 2
    true_count = 0
    # only really need to compare the lower edge of window 1
    # with upper edge of window 2. overlapping will always
    # be the same, so sum is dependent only on those edges
    lower_edge = 0
    upper_edge = 3
    while upper_edge < len(val_list):
        if val_list[lower_edge] < val_list[upper_edge]:
            true_count += 1
        lower_edge += 1
        upper_edge += 1
    print(true_count)
    

if __name__ == '__main__':
    main()