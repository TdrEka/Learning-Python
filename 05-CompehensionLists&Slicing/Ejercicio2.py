# Ejercicio slicing 1
# Crear una funcion que nos diga si un texto es palindromo o no lo es
import unicodedata
import re


text = input("Gimme a text to check whether its a palindrome: ")

def CheckPalindrome():
    cleantext = text.lower().replace(' ', '')
    palindrome = cleantext[::-1]
    if cleantext == palindrome:
        print("Your text is a palindrome.")
    else: print("That's not a palindrome")

CheckPalindrome()



#text = input("Gimme a text to check whether its a palindrome: ")
#
#
#def CheckPalindrome():
#    normalized = unicodedata.normalize('NFD', text.lower())
#    without_accents = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
#
#    cleantext = re.sub(r'[^a-z]', '', without_accents)
#
#    palindrome = cleantext[::-1]
#    if cleantext == palindrome:
#        print("Your text is a palindrome.")
#    else:
#        print("That's not a palindrome")
#
#
#CheckPalindrome()