divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

#Question 5.a
print("Question 5.a")
divided.update(we_fall)
united_we_stand={}

for key,value in divided.items():
    united_we_stand.update({key:value})

print(united_we_stand)

print("{:<10} {:<10} ".format('NAME', 'AGE'))
for key, value in united_we_stand.items():
    name=key
    age = value
    print("{:<10} {:<10} ".format(name,age))

print("Question 5.b")

del united_we_stand['Nat']

print("{:<10} {:<10} ".format('NAME', 'AGE'))
for key, value in united_we_stand.items():
    name=key
    age = value
    print("{:<10} {:<10} ".format(name,age))

print("Question 5.c")
united_we_stand = dict(sorted(united_we_stand.items()))
print("{:<10} {:<10} ".format('NAME', 'AGE'))
for key, value in united_we_stand.items():
    name=key
    age = value
    print("{:<10} {:<10} ".format(name,age))


print("Question 5.d")
united_we_stand = dict(sorted(united_we_stand.items(),key=lambda item:item[1]))
key_max = max(united_we_stand.values())
key_min = min(united_we_stand.values())
print(key_min)
print(key_max)



