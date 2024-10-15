age=int(input("Enter you age"))
if age < 10:
    print("The entry ticket fare is 7")
elif age >= 10 and age < 60:
    print("The entry ticket fare is 10")
elif age >= 60:
    print("The entry ticket fare is 5")
else:
    print("Your are not eligible for ticket")