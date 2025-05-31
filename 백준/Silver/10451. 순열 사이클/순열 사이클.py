def count_cycles_stack(n, m):
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i].append(m[i - 1])

    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            count += 1

    return count

t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(count_cycles_stack(n, m))
