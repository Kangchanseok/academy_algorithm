
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

n,m = map(int,input().split())
lst = [0 for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    lst[a-1:b] = [c] * (b-a+1)
print(*lst)
    