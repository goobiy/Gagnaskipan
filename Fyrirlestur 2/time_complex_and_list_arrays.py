import random
# import time
# def power(x, n):
#     for i in range(x**n):
#         print(i)
# power(2,10*50)



#2
# def multi_2_int(x:int, y:int)-> int:
#     total = 0
#     for i in range(y):
#         total += x
#     return total

# start_time = time.perf_counter()
# x = multi_2_int(100,50)
# end_time = time.perf_counter()

# print(x,"\t",(end_time-start_time)*1000)


# 3

# random_list = [7,8,9,10]

# for i in range(len(random_list)):
    
    # random_list[i] = random.randint(1,6)
# print(random_list)
# O(n)


#4

# def print_list(my_list: list) -> list:

#     for i in my_list:
#         if i != my_list[len(my_list)-1]:
#             print(i, end=", ")
#         else:
#             print(i)
#     return my_list

# print_list([2,3,100,-3,34])

# O(n)


# 5

# my_list = [0,1,2,3,4,5,6,7,8,9,10,11]


# for i in my_list:
#     random_number = random.randint(0,len(my_list))
#     my_list[i] = random_number

# print(my_list)


# 6

a_list = []

for i in range(random.randint(1,12)):
    random_number = random.randint(1,100)
    a_list.append(random_number)

print(a_list)
random_index = random.randint(0,(len(a_list)-2))  # not the last index
print(len(a_list))
print(random_index)
a_list[random_index] = a_list[random_index-1]

print(a_list)

# vantar að switcha valueinu í random_index location með því sem er í slottinu á undan
# líka að switcha tveim stökum sem eru í random stöðum