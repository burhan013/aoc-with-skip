
def dodoo(block):
    biggest = 0

    for i in range(len(block)):
        for j in range(i+1, len(block)):
            combo = int(block[i] + block[j])
            if combo > biggest:
                biggest = combo
                combined = block[i] + block[j]

    return int(combined)





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
        counter += dodoo(block)
    print(f"The total is: \n\n{counter}")




if __name__ == "__main__":
    main()