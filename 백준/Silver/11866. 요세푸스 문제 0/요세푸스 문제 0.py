from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))  # 1번부터 n번까지 사람을 큐에 넣음

result = []

while q:
    q.rotate(-(k - 1))  # k-1만큼 왼쪽으로 회전 (k번째가 맨 앞에 오도록)
    result.append(q.popleft())  # 맨 앞 사람 제거

# 결과 출력 형식에 맞게 출력
print("<" + ", ".join(map(str, result)) + ">")
