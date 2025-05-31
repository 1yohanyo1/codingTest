def find_cycles(permutation):
    visited = [False] * (len(permutation) + 1)
    count = 0

    for i in range(1, len(permutation)):
        if not visited[i]:
            count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = permutation[current]
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    perm = [0] + list(map(int, input().split()))
    print(find_cycles(perm))
