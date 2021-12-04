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


def val_removal(vals, bit):
    purged_vals = []
    for i in vals:
        if i[0] == bit:
            purged_vals.append(i)
        else:
            print("This should never print")
    return purged_vals


def val_parsing(vals, is_generator):
    length = len(vals[0]) # setting comparison length
    values = vals
    while len(values) > 1:
        print(len(values))
        for char_index in range(length):
            t_count = 0
            f_count = 0
            for binary in values:
                # print(binary)
                if len(binary) == length:
                    if binary[char_index] == '1':
                        t_count += 1
                    else:
                        f_count += 1
                else:
                    print('Length not matching for all inputs')
            if t_count > f_count:
                if is_generator:
                    values = val_removal(values, '1')
                    print('this works')
                else:
                    values = val_removal(values, '0')
            elif t_count == f_count:
                if is_generator:
                    values = val_removal(values, '1')
                else:
                    values = val_removal(values, '0')
            else:
                if is_generator:
                    values = val_removal(values, '0')
                else:
                    values = val_removal(values, '1')
    return vals

def part_two(vals):
    oxygen_gen = vals
    coo_scrub = vals
    val_parsing(oxygen_gen, True)



def main():
    vals = fileload('input')
    part_one(vals)
    part_two(vals)


if __name__ == "__main__":
    main()