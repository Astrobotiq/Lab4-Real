a = 1
dict = {}
#Q4.a
print("Question 4.a \n")
while a < 31:
    value = (a+1)*(a-1)
    dict.update({a:value})
    a+=1

print(dict)
#Q4.b
print("Question 4.b \n")
for x in dict.items():
    print(x)

#Q4.c
print("Question 4.c \n")
totalValues = 0
for x in dict.values():
    totalValues+=x
print(totalValues)

#Q4.d
print("Question 4.d \n")
while True:
    numToDel = int(input("Give me a key number"))
    if numToDel in dict.keys():
        dict.pop(numToDel)
        break

print(dict)