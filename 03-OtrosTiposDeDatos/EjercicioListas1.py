#Ejercicio 1
#Ask an user for numbers one by one to add them
#The sum has to happen when the user doesnt wanna add more numbers
#The loop stops when user enter "Exit"

numbers = []
total = 0
while True:
    user_input = input("Enter a number (or 'Exit' to stop): ")

    if user_input.lower() == "exit":
        break

    num = float(user_input)
    numbers.append(num)
    total += num

print(f"Numbers entered: {numbers}")
print(f"Final sum: {total}")


