
# s = int(input())
# s2 = input()
# s3 = input()
# s4 = input()
# s5 = input()
# s6 = input()


# print(s,s2)


# n = int(input())

# s1,s2,s3,s4,s5 = input().splitlines()
# print(s3)
# for i in range(n):
#     s = input()
#     print(s)


# a,b,c = map(int,input().split())
# print(b)

# 10810

# n,m = map(int,input().split())
# lst = [0 for i in range(n)]
# for i in range(m):
#     a,b,c = map(int,input().split())
#     lst[a-1:b] = [c] * (b-a+1)
# print(*lst)
    

# word = input()
# alphabet = list(range(97,123)) # 아스키코드에서 a는 97이고 z 는 122임
# for x in alphabet :
#     print(word.find(chr(x))) 

# n = int(input())
# for _ in range(n):
#     r, s = input().split()
#     for i in s:
#         i += i*(int(r)-1)
#         print(i, end='')

# n = int(input())
# for i in range(n):
#     a,b = input().split()
#     st = ''
#     for j in b:
#         st += int(a) * j
#     print(st)
    
# 2747
# n = int(input())
# def pibo(x):
#     if x < 2:
#         return x
#     else:
#         return pibo(x-2) + pibo(x-1)

# print(pibo(n))
                

n,m = map(int, input().split())
lst = [_ for _ in range(1,n+1)]
for i in range(m):
    a,b = map(int, input().split())
    temp = lst[a-1:b]
    temp.reverse()
    lst[a-1:b] = temp
print(*lst)
