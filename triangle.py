limit=int(input("Enter the limit"))
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#increasing order
for i in range(limit):
    for j in range(i):
        print("*",end=" ")
    print()
print(" ")
#hill pattern
for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print(" ")
#reverse hill pattern
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()