unConjunto = set([1, 2, 3, 4, 5, 6, 4, 951, 443, 34, 1996, 4, 17])
print(unConjunto)
print(len(unConjunto))

otroConjunto = {4, 5, 6, 7, 8, 5, 6, 9, 4, 28, 32, 45, 55}
print(type(otroConjunto))

item = otroConjunto.pop()
print(item)
print(otroConjunto)

otroConjunto.add(item)
otroConjunto.add(9)
print(otroConjunto)

unConjunto.update(otroConjunto)
print(unConjunto)

unConjunto.discard(10)
# unConjunto.remove(10) da error si el elemento no esta presente

print(unConjunto.union(otroConjunto))

unConjunto = {1, 2, 3, 4, 5}
otroConjunto = {4, 5, 6, 7, 8, 9}
print(unConjunto.intersection(otroConjunto))
print(unConjunto.difference(otroConjunto))
print(unConjunto.symmetric_difference(otroConjunto))
