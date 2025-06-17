# Ejercicio slicing 1
# Crear una funcion que nos diga si un texto es palindromo o no lo es

text = input("Gimme a text to check whether its a palindrome: ")

def CheckPalindrome():
    cleantext = text.lower().replace(' ', '')
    palindrome = cleantext[::-1]
    if cleantext == palindrome:
        print("Your text is a palindrome.")
    else: print("That's not a palindrome")

CheckPalindrome()