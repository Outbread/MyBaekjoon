n = int(input())
def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result
print(factorial(n))

#for문 이용!
# n= int(input())
# result2 = 1
# if n > 0:
#     for i in range(1, n+1):
#         result2 *= 1
# print(result2)