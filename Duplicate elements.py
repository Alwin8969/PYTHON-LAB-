list=[10,35,76,48,10,76]
orginal=[]
for n in list:
    if n not in orginal:
        orginal.append(n)
print("The orginal number is:",list)
print(orginal)