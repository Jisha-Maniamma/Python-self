name="jisha"

print(name[0:100000:2])

number="9,233,455,667,788"
seperator=number[1::4]
print(seperator)
values="".join(char if char not in seperator else " " for char in number).split()
print(values)
print([int(val) for val in values])

""" spliicing  backwards """


print(name[5::-1])
print(name[::-1])


myString="abcdefghijklmnopqrstuvwxyz"
# qpo
print(myString[16:13:-1])
# edcba
print(myString[4::-1])
# last 8 charachters in reverse order
print(myString[25:17:-1])
print(myString[:-9:-1])

print(name[:-3:-1])
print(name[-3:])
print(name[-1:])
print(name[:1])

name=""
print(name[:1])
print("....")
print(name[0]) #this throws an error
