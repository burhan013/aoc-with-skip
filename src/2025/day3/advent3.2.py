def crashout(block):
    target = 12
    size = len(block)

    deletion = size - target
    hit = []

    for digit in block:
        while deletion > 0 and len(hit) > 0 and digit > hit[-1]:
            hit.pop()
            deletion -= 1
        hit.append(digit)
    
    if deletion > 0:
        hit = hit[:-deletion]

    return int("".join(hit))



#987654321111111 9, 8
#811111111111119 8, 9
#234234234234278 7, 8
#818181911112111 9, 2



def main():
    counter = 0
    with open("bruhhhh.txt", "r") as f:
        text = f.read().strip()
    listOfNums = [line.strip() for line in text.splitlines() if line.strip()]
    for block in listOfNums:
        counter += crashout(block)
    print(f"The total is: \n\n{counter}")




if __name__ == "__main__":
    main()