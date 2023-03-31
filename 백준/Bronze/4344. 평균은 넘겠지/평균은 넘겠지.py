c = int(input())

for i in range(c):
    s = list(map(int, input().split()))
    cnt = 0
    avg = sum(s[1:])/s[0]
    for j in s[1:]:
        if avg < j:
            cnt += 1
    r = cnt/s[0]*100
    print(f'{r:.3f}%')