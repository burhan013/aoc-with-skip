

def reader(rotation, code):

    rotation = rotation.lower()
    direction = rotation[0]
    number = int(rotation[1:])
    

    for r in range(1):
        if direction == "l":
            code = (code - number) % 100
            # if code < 0:
            #     code = code + 100
        elif direction == "r":
            code = (code + number) % 100
            # if code > 99:
            #     code = code - 100
    
    return code
        

def count_the_zeros(count):
    if count == 0:
        return + 1
    else:
        return 0
        
def file_reader():
    pass


def main():
    code = 50
    counter = 0
    print(f"The dial starts at {code}")

    with open("rotations.txt") as f:
        for line in f:
            rotations = line.strip()
            if not rotations:
                continue
            code = reader(rotations, code)
            counter += count_the_zeros(code)
            print(f"The dial is rotated {rotations} to point at {code}")
    
    print(f"0 appeared: {counter} times")




if __name__ == "__main__":
    main()