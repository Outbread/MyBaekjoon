
for i in range(int(input())):
    q = list(input())
    score = 0
    sum = 0
    for j in q:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)