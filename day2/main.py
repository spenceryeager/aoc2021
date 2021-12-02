
def main():
    # file opening
    file = open("day2/input", "r")
    vals = []
    for value in file:
        vals.append(value.strip("\n"))
    file.close()

    # part 1
    x_pos = 0
    z_up = 0
    z_down = 0

    for i in vals:
        if i[0] == 'f':
            x_pos += int(i[-1])

        elif i[0] == 'u':
            z_up += int(i[-1])

        elif i[0] == 'd':
            z_down += int(i[-1])
    
    print(x_pos * (z_down - z_up))

    # part 2

if __name__ == "__main__":
    main()