def mobile():
    num=input("Enter the mobile num:")
    if len(num)==10 and num[0] in ("7","8","9"):
        print("Number is valid")
    else:
        print("NUmber is not valid")
mobile()