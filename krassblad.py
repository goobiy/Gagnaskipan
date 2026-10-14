from collections import deque


# from collections import deque

# d = deque([20,50,40],maxlen=4)
# print(d)
# d.append(10)
# d.appendleft(30)
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)
# print("-"*100)
# # d.appendleft(200)
# # print(d)
# # d.appendleft(0)
# # print(d)
# # d.appendleft(60)
# # print(d)
# # d.appendleft(70)
# # print(d)
# # d.append(1000)
# # print(d)
# # d.append(300)
# # print(d)

# def prefix_sum(a: list[int]):
#     ps = []

#     for i in range(len(a)):
#         s = sum(a[:i+1])
#         ps.append(s)
#     return ps


# def hanoi(n, source, target, auxiliary):
#     if n == 0:                          # base case
#         return
#     hanoi(n-1, source, auxiliary, target)   # step 1
#     print(f"Move disk {n}: {source} → {target}")  # step 2
#     hanoi(n-1, auxiliary, target, source)   # step 3

# hanoi(3, 'A', 'C', 'B')





def is_palindrome(s: str) -> bool:
    d = deque()
    check = ""

    for l in s[::-1]:
        d.append(l)

    counter = 0
    for e in d:
        check += d[counter]
        counter += 1

    return s == check

print(is_palindrome("hello"))