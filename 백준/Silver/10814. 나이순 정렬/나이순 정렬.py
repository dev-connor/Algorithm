n = int(input())
users = []
for _ in range(n):
    a,b = input().split()
    users.append((int(a),b))
users.sort(key=lambda x:x[0])
for user in users:
    print(user[0],user[1])