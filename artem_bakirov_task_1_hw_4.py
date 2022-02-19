str1 = input('Введите строку:')
if len(str1) <= 2:
    print('Ваша строка слишком короткая - "%s".' % str1)
if str1 == 'Hillel school':
    a = 'Hillel school'[0:2]
    b = 'Hillel school'[11:]
    print(a + b)
