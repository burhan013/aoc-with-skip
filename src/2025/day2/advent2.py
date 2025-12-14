




with open("bruh.txt", "r", encoding="utf-8") as f:
    first = f.read().strip()
    count = 0

    for bruh in first.split(","):

        before = bruh.split('-')[0] #before -
        after = bruh.split('-')[1] #after -

        print(before, after)

        
        for i in range(int(before), int(after)+1):
            halfer = len(str(i)) // 2
            if str(i)[:halfer] == str(i)[halfer:]:
                print(str(i) + " This is identical")
                count = count + i
                print(f"New count: {count}")
        
