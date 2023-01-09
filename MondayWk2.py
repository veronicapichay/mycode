#!/usr/bin/python3
"""Challenge 67 | Looping Variable"""

def vampytimes_maker(line):
    """write lines into a file if they contain vampire"""

    #line may or may not end in a "\n"
    line = line.rstrip()
    line = line + "\n"

    with open ("vampytimes.txt", "a") as vamp_file:
        vamp_file.write(line)

    return line.rstrip() # end of fx, return the line exactly as it was in a file 

def main():
    """runtime"""

    count_dracula = 0

    with open("dracula.txt") as dracula:
        for line in dracula:
            if "vampire" in line.lower():
                count_dracula += 1 # add 1 to counter
                print(vampytimes_maker(line), end="")

    print("Total number of lines with the word vampire: ", count_dracula)


if __name__ == "__main__":
    main()




