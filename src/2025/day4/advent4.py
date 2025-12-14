

### (-1,-1), (-1, 0), (-1, 1),
### (0, -1), (0, 0), (0, 1),
### (1, -1), (1, 0), (1, 1)
with open("hmm.txt", "r") as f:
    grid = [line.strip() for line in f if line.strip()]

rows = len(grid)
cols = len(grid[0])
rolls = 0
out = [list(row) for row in grid]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue

        max_rolls = 4
        for delta_r in (-1, 0, 1):
            for delta_c in (-1, 0, 1):
                if delta_r == 0 and delta_c == 0:
                    continue
                
                adjacent_r = r + delta_r
                adjacent_c = c + delta_c

                if 0 <= adjacent_r < rows and 0 <= adjacent_c < cols:
                    if grid[adjacent_r][adjacent_c] == "@":
                        max_rolls -= 1

        if max_rolls > 0:
            out[r][c] = "x"
            rolls += 1 





for row in out:
    print("".join(row))

print(f"Rolls O' Paper: {rolls}")
