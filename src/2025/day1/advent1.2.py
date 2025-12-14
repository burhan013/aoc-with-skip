

def reader(rotation, code):

    rotation = rotation.lower()
    direction = rotation[0]
    number = int(rotation[1:])

    zeros_hits = 0
    
    for _ in range(number):
        if direction == "l":
            code = (code - 1) % 100
        elif direction == "r":
            code = (code + 1) % 100

        if code == 0:
            zeros_hits += 1
    
    return code, zeros_hits
        

def main():
    code = 50
    counter = 0
    print(f"The dial starts at {code}")

    with open("rotations.txt") as f:
        for line in f:
            rotations = line.strip()
            if not rotations:
                continue
            code, zeros = reader(rotations, code)
            counter += zeros
            print(f"The dial is rotated {rotations} to point at {code}")
    
    print(f"0 appeared: {counter} times")




if __name__ == "__main__":
    main()