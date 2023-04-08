def queen(row):
    if row == N: # 모든 행에 퀸을 놓았으므로 res 1 증가시키고 종료 
        global res
        res += 1
        return

    for i in range(N): # 0열 ~ N-1열 까지
        if check[i]: # 이미 사용된 열이면 continue 
            continue 

        board[row] = i # row행 i열에 퀸을 놓는다 

        possible = True 
        for j in range(row): # 0행 부터 row-1행 까지 돌면서
            # 같은 열에 놓았는지, 같은 대각선 상에 놓았는지를 체크 
            if board[row] == board[j] or (row - j == abs(board[row] - board[j])):
                possible = False # 공격할 수 있는 위치면 놓을 수 없음을 체크하고 break
                break 
        
        if possible: # 가능한 위치에 놓였을 경우 
            check[i] = True 
            queen(row+1) # 다음 행에 대하여 반복 수행 
            check[i] = False 


if __name__ == '__main__':
    N = int(input())
    check = [False for _ in range(N)] # 해당 열이 사용되었는지를 체크하기 위한 리스트
    board = [0 for _ in range(N)] # board[n] = m은 n행 m열에 퀸을 놓았음을 의미한다 
    res = 0

    queen(0)

    print(res)