def count_upper_lower_case_characters(input_string):
    upper_characters=0
    lower_characters=0
    for character in input_string:
        if character.isupper():
            upper_characters+=1
        else:
            lower_characters+=1
    print(upper_characters,lower_characters)
    return upper_characters,lower_characters


input_string=input("Enter the string")
upper_character,lower_character=count_upper_lower_case_characters(input_string)
