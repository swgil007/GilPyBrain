a = 1 + 22
b = "gillog"

print(a)
print(b)


def sum(a, b):
    return a + b


print(sum(1, 22))

def sumMany(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

sumOneToTen = sumMany(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sumOneToTen)

a = "gil"
b = "log"
c = "python"

print (a+b+ c)
print((a+b) * 2)

# 튜플

tuple1 = (1, "gil")
tuple2 = (2, "log")

tuplePlus = tuple1 + tuple2

tupleMultiple = tuple1 * 3

tupleIndex = tuple1[0]

print(tuple1)
print(tuple2)
print(tuplePlus)
print(tupleMultiple)
print(tupleIndex)
