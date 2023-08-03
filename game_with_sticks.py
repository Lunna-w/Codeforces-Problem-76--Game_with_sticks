n, m = list(map(int, input().split()))

total_moves = min(n, m)

if total_moves % 2 == 0:
    print("Malvika")
else:
    print("Akshat")