def fileload(input):
    file = open(input, 'r')
    vals = []
    for line in file:
        line = line.split('\n')
        vals.append(line[0])
    return vals


def eps(gamma):
    epsilon = ''
    for char in gamma:
        if char == '1':
            epsilon = epsilon + '0'
        else:
            epsilon = epsilon + '1'
    return epsilon


def part_one(vals):
    gamma = '' # initializing gamma val as blank string for concatenation
    length = len(vals[0]) # setting comparison length

    for char_index in range(length):
        t_count = 0
        f_count = 0
        for binary in vals:
            if len(binary) == length:
                if binary[char_index] == '1':
                    t_count += 1
                else:
                    f_count += 1
            else:
                print('Length not matching for all inputs')

        if t_count > f_count:
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'
    
    epsilon = eps(gamma)
    print(int(gamma, 2) * int(epsilon, 2))


def main():
    vals = fileload('input')
    part_one(vals)


if __name__ == "__main__":
    main()