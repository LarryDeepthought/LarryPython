
def main():
    """
    Main function
    """
    # Read the input
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Read the dots
    dots = []
    for line in lines[1:]:
        x, y = line.split(",")
        dots.append((int(x), int(y)))

    # Read the instructions
    instructions = []
    for line in lines[len(lines) - 1:]:
        instructions.append(line.strip())

    # Compute the result
    result = 0
    for instruction in instructions:
        if instruction.startswith("y="):
            y = int(instruction.split("=")[1])
            for dot in dots:
                if dot[1] == y:
                    result += 1
        else:
            x = int(instruction.split("=")[1])
            for dot in dots:
                if dot[0] == x:
                    result += 1

    # Print the result
    print(result)


if __name__ == "__main__":
    main()