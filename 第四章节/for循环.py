for value in range(1,21):#4-3
    print(value)



numbers = list(range(1,1000001))#4-4到4-5
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))


odd_numberss = list(range(1,21,2))#4-6
print(odd_numberss)

there_numbers = list(range(3,31,3))#4-7
print(there_numbers)

squares = []#4-8
for value in range(1,11):
    square = value**3
    squares.append(square)
print(squares)

lifang = [value**3 for value in range(1,11)]#4-9
print(lifang)