n = int(input())
contacts = {}
for i in range(n):
    detail = input().split()
    contacts[detail[0]] = detail[1]

for _ in range(n):
    name = input().strip()
    if name in contacts:
        print(name+"="+contacts[name])
    else:
        print("Not found")
