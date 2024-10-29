string_input=input("Enter a string")
vowels=("aeiouAEIOU")
vowels_count=0
for char in string_input:
    if char in vowels:
        print(char)
        vowels_count+=1
print(f"No of vowels in the given string{vowels_count}")