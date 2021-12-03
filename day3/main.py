def fileload(input):
    file = open(input, 'r')
    vals = []
    for line in file:
        line = line.split('\n')
        vals.append(line[0])
    return vals


def part_one(vals):
    gamma = ''
    length = len(vals[0])
    

    for char_index in range(length):
        t_count = 0
        f_count = 0
        for binary in vals:
            if len(binary) == length:
                print(char_index)
            else:
                print('Length not matching for all inputs')

    # for binary in vals:

        

def main():
    vals = fileload('input')
    part_one(vals)


if __name__ == "__main__":
    main()