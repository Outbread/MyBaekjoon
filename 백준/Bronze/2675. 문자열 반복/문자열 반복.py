for i in range(int(input())):
    r, s = input().split()
    txt = ""
    for i in s:
        txt += int(r) * i
    print(txt)