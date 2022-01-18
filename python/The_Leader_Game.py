n = int(input())
p1 = 0
p2 = 0
lead = 0
for i in range(n):
    score1, score2 = map(int, input().split())
    p1 = p1 + score1
    p2 = p2 + score2
    diff = p1 - p2

    if diff > 0 and diff > lead:
        lead = diff
        leader = 1
    elif diff < 0 and abs(diff) > lead:
        lead = abs(diff)
        leader = 2
print(leader,lead)