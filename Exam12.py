import random
n = int(input("Type a number between 15 and 35: "))

while n < 15 or n > 35:
    
    
    print("Invalid output.")

    n = int(input("Type a number between 15 and 35: "))

        

list1 = []

for i in range(n):
    list1.append(random.randint(30, 300))
print(list1)

for i in range(len(list1)):
    digit = str(list1[i])[-2]
    if int(digit) % 3 == 0:
        print(list1[i])

minIndex = 300
min = 301
for i in range(len(list1)):
    if list1[i] % 6 == 4:
        if min > list1[i]:
            min = list1[i]
            minIndex = i

print(minIndex)

list2 = []
for i in range(len(list1)):
    if len(str(list1[i])) == 2 and (list1[i] % 2 == 0 or list1[i] % 3 == 0):
        list2.append(list1[i])
print(list2)

sum = 0
count = 0
for i in range(1, len(list2), 2):
    sum += list2[i]
    count += 1

print(format("%.2f") % (sum / count))


minEven = 300
for i in range(len(list2)):
    if list2[i] % 2 == 0 and list2[i] < minEven:
        minEven = list2[i]

list2.remove(minEven)
print(list2)
