# Make a recursive function that sums a list and returns the total value (try nested lists if feeling spicy)

list1 = [1, 2, 3, 4, 5, 6]


def sum_recursive(lists):
    if len(lists) == 0:
        return 0
    else:

        return lists[0] + sum_recursive(lists[1:])


print(sum_recursive(list1))

def sum_spicy(lists):
    if len(lists) == 0:
        return 0
    elif isinstance(lists[0], list):
        return sum_spicy(lists[0]) + sum_spicy(lists[1:])
    else:
        return lists[0] + sum_spicy(lists[1:])

nested_list = [1, [2, 3], 4, [5, [6, 7]]]
print(sum_spicy(nested_list))