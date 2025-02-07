setter = input('enter somthing: ')
list_1 = []
list_2 = []
setter = setter.replace(',', '')
for x in setter:
    list_1.append(x)
    list_2.append(x)
list = list_1
tuple = tuple(list_2)
print(list)
print()
print(tuple)