
def solve(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    elves = list()

    len_lines = len(lines)

    i = 0

    while i < len_lines:
        elf = 0

        # Store weights per elf
        while i < len_lines and lines[i] != '\n':
            elf += int(lines[i].replace('\n', ''))
            i += 1

        # Move onto the next elf
        elves.append(elf)
        i += 1

    # Sort in descending order
    elves = sorted(elves, reverse=True)
    
    # Display sum of top 3 elves
    print(elves)
    print(sum(elves[0:3]))



if __name__ == '__main__':
    solve('d1.input')
