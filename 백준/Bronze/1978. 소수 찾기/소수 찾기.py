#소수찾기

n = int(input())

num = map(int, input().split())

cnt = 0

for p in num:
    '''1은 소수가 아니므로 2부터 시작한다. '''
    for j in range(2, p+1):
        '''j가 소수 p까지 for문으로 돌며 p와 나눠떨어지는지 검사한다.'''
        if p % j == 0:
            '''p에 도달하지 못하고 중간에 나눠떨어지면 소수가 아니므로 break해주고'''
            if p == j:
                '''p에 도달후 나눠떨어지면 소수이므로 cnt + 1을 해준다.'''
                cnt += 1
                
            break
print(cnt)