import re
x=input('Masukkan operasi matematika (+, -, *, /, ^, %): ')
pat=re.match("^(\d+\.?\d*[\+\-\*\/\^\%])(\d+\.?\d*[\+\-\*\/\^\%])*\d+$",x)
if pat:
    print(eval(x))
else:
    print('Operation invalid')