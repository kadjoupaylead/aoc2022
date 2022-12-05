
def solve(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    i = 0
    len_lines = len(lines)

    max_cals = -1

    while i < len_lines:
        elf = 0
        # Collect all weights for current elf
        while i < len_lines and lines[i] != "\n":
            elf += int(lines[i].replace("\n", ""))
            i += 1

        # Compare & store if superior to the max
        if elf > max_cals:
            max_cals = elf

        i += 1

    print(max_cals)


if __name__ == '__main__':
    solve('d1.input')
