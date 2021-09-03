# n = int(input())
# l = []
# for i in range(n):
#     tmp = int(input())
#     l.append(tmp)
# mini = l[0]
# index = 0
# for i in range(1 , n):
#     if l[i] < mini:
#         mini = l[i]
# print(l)
# print(mini , index)













# n = int(input())
# l = []
# ans = []
# for i in range(n):
#     tmp = int(input())
#     l.append(tmp)
# for i in range(n):
#     mini = l[0]
#     index = 0
#     for j in range(n):
#         if mini > l[j]:
#             mini = l[j]
#             index = j
#     ans.append(mini)
#     del l[index]
#     print('l:' , l)
#     print('ans:' , ans)




















# n = int(input())
# l = []
# for i in range(n):
#     tmp = int(input())
#     l.append(tmp)
# for i in range(n):
#     maxi = l[0]
#     index = 0
#     for j in range(n - i):
#         if maxi < l[j]:
#             maxi = l[j]
#             index = j
#     tmp = l[index]
#     l[index] = l[n-1-i]
#     l[n - 1 - i] = maxi
#     print('l:' , l)
#     print()









# l = [-2 , 2 , 10 , 200 , 320]
# a = int(input())
# n = len(l)
# l.append(a)
# for i in range(n):
#     if (l[n - i] < l[n - 1 - i]):
#         l[n - i] , l[n - 1 - i] = l[n - 1 - i] , l[n - i]
#     else:
#         break
# print(l)













# l = []
# n = int(input())
# for i in range(n):
#     tmp = int(input())
#     l.append(tmp)
# ans = [l[0]]
# for j in range(1 , n):
#     n = len(ans)
#     ans.append(l[j])
#     print(ans)
#     for i in range(n):
#         if (ans[n - i] < ans[n - 1 - i]):
#             ans[n - i] , ans[n - 1 - i] = ans[n - 1 - i] , ans[n - i]
#         else:
#             break
#     print(ans)
#     print()










# l = []
# n = int(input())
# for i in range(n):
#     tmp = int(input())
#     l.append(tmp)
# for j in range(1 , n):
#     n = j
#     for i in range(n):
#         if (l[n - i] < l[n - 1 - i]):
#             l[n - i] , l[n - 1 - i] = l[n - 1 - i] , l[n - i]
#         else:
#             break
#     print(l)
#     print(l[0:j])
#     print()













# n = int(input())
# l = []
# for i in range(n):
#     l.append(input())
# for i in range(n):
#     for j in range(n-1-i):
#         if(l[j] > l[j + 1]):
#             l[j] , l[j + 1] = l[j + 1] , l[j]
# print(l)











# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# b = []
# for i in range(10):
#     b.append(0)
# for i in range(n):
#     tmp = l[i]
#     b[tmp] = b[tmp]+1
# l = []
# for i in range(9 , -1 , -1):
#     for j in range(b[i]):
#         l.append(i)
# print(l)














# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# b = []
# for i in range(12):
#     b.append(0)
# for i in range(n):
#     tmp = l[i]
#     b[tmp+5] = b[tmp+5]+1
# l = []
# for i in range(11 , -1 , -1):
#     for j in range(b[i]):
#         l.append(i - 5)
# print(l)








n = int(input())
l =[]
for i in range(n):
    l.append(input())
a = int(input())
for i in range(n):
    if(l[i] == a):
        print(i)
