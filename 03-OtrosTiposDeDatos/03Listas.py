una_lista = [1, 'abc', 9.36, ['amarillo'], True]
una_lista_vacia = list()

lista_nums = [1, 2, 3, 4]
print(lista_nums[2])

lista_nums[2] = 7
print(lista_nums)

texto = 'hola'
print(list(texto))

lista_nums = list([1, 2, 3, 4])
print(lista_nums)


print(list([texto]))

user1 = 'Mike'
user2 = 'Octavia'
user3 = 'Charlie'

onlineUsers = []

print(onlineUsers)
onlineUsers.append(user1)
onlineUsers.append(user2)
print(onlineUsers)

onlineUsers.append(user3)
print(onlineUsers)

if user2 not in onlineUsers:
    onlineUsers.append(user2)
    print("user2 just logged in")
else:
    print(f"User {user2} is already online")

print(onlineUsers)


recentUser = onlineUsers.pop()

print(recentUser)
print(onlineUsers)

matriz = [
    [[1, 2, 3], [0, 0, 0], [9, 8, 7]],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])
print(matriz[0])
print(matriz[0][2][0])


