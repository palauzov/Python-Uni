import random

n = int(input("Type a number between 20 and 30: "))
if n <= 20 or n >=30:
    print("Invalid input.")
    exit()

list1 = []
for i in range(n):
    list1.append(random.randint(-100, 100))
print(list1)
sumOfOdss = 0
for i in range(1, len(list1), 2):
    sumOfOdss += list1[i]

print(sumOfOdss)

countOfEven = 0
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        countOfEven += 1

print(countOfEven)

m = 1

for i in range(len(list1)):
    if list1[i] < 0 and list1[i] % 2 == 0:
        m*=list1[i]
print(m)

list1.sort(reverse=True)
print(list1)

list2 = []
for i in range(len(list1)):
    if list1[i] > n:
        list2.append(list1[i])

print(list2)

d = list2[0] - list2[len(list2) - 1]
print(d)

lisOfOdds = []
countOfOdds = 0

for i in range(len(list2)):
    if list2[i] % 2 == 1:
        lisOfOdds.append(list2[i])
        countOfOdds += 1

print(lisOfOdds)
print("Count of odds is", countOfOdds)

list2.sort()
list2.remove(list2[0])

print(list2)
