import numpy as np


def main():
    # input file
    vals = np.genfromtxt("day1/input.csv", delimiter=",")
    
    true_count = 0
    comp_val = vals[0]
    
    index = 1
    while index < len(vals):
        if (vals[index] - comp_val) > 0:
            true_count += 1
        comp_val = vals[index]
        index += 1

    print(true_count)

if __name__ == '__main__':
    main()