
def check_it(i):
    stringer = str(i)
    strlen = len(stringer)

    for slice_size in range (1, (strlen // 2) + 1):
        if strlen % slice_size != 0:
            continue
        multiples = strlen // slice_size
        sliced = stringer[:slice_size]
        if multiples >= 2 and multiples * sliced == stringer:
            return True

    return False


def main():

    with open("bruh.txt", "r") as f:
        first = f.read().strip()
        count = 0

        for bruh in first.split(","):

            before = bruh.split('-')[0] #before -
            after = bruh.split('-')[1] #after -
            
            for i in range(int(before), int(after)+1):
                if check_it(i):
                    print(str(i) + " <- This is identical")
                    count = count + i
                    print(f"New count: {count}")



if __name__ == "__main__":
    main()
