

num_friends = int(input())


friends = []
for i in range(num_friends):
    friend_age = int(input())
    friends.append(friend_age)

print(min(friends))