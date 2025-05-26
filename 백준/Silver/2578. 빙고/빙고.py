import sys
input = sys.stdin.readline

position = {}
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        position[row[j]] = (i, j)

called_numbers = []
for _ in range(5):
    called_numbers += list(map(int, input().split()))

row_mask = [0] * 5
col_mask = [0] * 5
diag1_mask = 0
diag2_mask = 0

for idx, num in enumerate(called_numbers):
    x, y = position[num]

    row_mask[x] |= (1 << y)
    col_mask[y] |= (1 << x)
    if x == y:
        diag1_mask |= (1 << x)
    if x + y == 4:
        diag2_mask |= (1 << x)

    bingo = 0
    for i in range(5):
        if row_mask[i] == 0b11111:
            bingo += 1
        if col_mask[i] == 0b11111:
            bingo += 1
    if diag1_mask == 0b11111:
        bingo += 1
    if diag2_mask == 0b11111:
        bingo += 1

    if bingo >= 3:
        print(idx + 1)
        break
