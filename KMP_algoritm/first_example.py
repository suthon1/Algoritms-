def liner_search_function(array, element):
    array.append(element)
    index = 0
    while array[index] != element:
        index += 1
    array.pop()
    if index != len(array):
        return index
    return -1


print(liner_search_function([1,2,3,4,5,7],3))

# another way to create with function and for loop
def liner_search_algoritm(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    raise IndexError('Not found')  #  or we can just return -1


print(liner_search_algoritm([1,2,3,4,5],3))
print(liner_search_algoritm([1,2,3,4,5],7))
