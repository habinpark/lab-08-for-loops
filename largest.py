largest = 0
for i in range(4):
    number = float(input('Number please: '))
    if number > largest:
        largest = number
print("The largest number is", largest)
