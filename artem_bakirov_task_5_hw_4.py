list1 = input('Введите слова:')
list2 = list1.split()
list3 = sorted(list2)
del list3[1:4:2]
print(list3)