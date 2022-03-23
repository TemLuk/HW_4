import collections

hillel_string = 'Hillel school'
string_length = print("Длинна вашей строки: " + str(len(hillel_string)))
hillel_dict = dict(collections.Counter(hillel_string))
print(hillel_dict)