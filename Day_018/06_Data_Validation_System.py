'''
6.Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
'''

char = input("Enter The Character = ")

Input = "Alphabet" if ('a'<= char <= 'z') or ('A' <= char <='Z') else "Digit" if '0' <= char <= '9' else "Special Character" 
 
print(Input)



