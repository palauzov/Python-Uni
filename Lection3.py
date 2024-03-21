data = [ -1, 10, 11, -32, 14]
data.sort()
print(data)

dataMatrix = [
    [1,2,3],
    [4,5]
]
print(dataMatrix)

for i in range(2):
    for j in range(len(dataMatrix[i])):
        print(dataMatrix[i][j], end = " ")
        print()


dataStudent = [
    [123, "Ivan", 5.65],
    [222, "Petar", 5.35],
    [333, "Lili", 6.00]
]

print(data)
dataStudent.sort(key = lambda st:[2], reverse= True)
print(dataStudent)

print(sorted.__doc__)
#print(sorted.__annotations__)

EURO = 1.95583
currency_in = input("Currency: ")
value_in = float(input("Value: "))

if currency_in == "BGN":
    currency_out = "EUR"
    value_out = value_in*EURO
elif currency_in == "EUR":
    currency_out = "BGN"
    value_out = value_in/EURO
else:
    print("Not supported...")
    exit()
    
print(value_out, currency_out)


stack = [1,2,3]
stack.append(44)
print(stack)
print(stack.pop())
print(stack)


queue = [4,5,6]
queue.insert(0,44)
print(queue)
queue.pop(0)
print(queue)

data = [int(x) for x in input("Data: ").split(",")]
print(data)


