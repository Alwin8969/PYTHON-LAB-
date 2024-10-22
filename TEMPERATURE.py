temp=float(input("Enter the temperature"))
ch=input("Is this in C/F? ")
if ch== "C" or ch == 'c':
    f=(9/5 *temp)+32
    print(f,"temp is in fahrenheit")
else:
    c=(5/9 *(temp-32))
    print(c,"temp is in celsius")