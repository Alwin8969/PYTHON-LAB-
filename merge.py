print("Enter the elements of lst1:")
for i in range(lst_size):
    lst1.append(int(input()))
lst_size_2=int(input("Enter the size of lst2="))
print("Enter the elements in lst2:")
for i in range(lst_size_2):
    lst2.append(int(input()))
print(lst1,lst2)
lst3=lst1+lst2
print(lst3)
odd_lst=[]
even_lst=[]
for i in lst3:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst)
print(odd_lst)
odd_lst.sort()
even_lst.sort()
final=odd_lst+even_lst
print(final)