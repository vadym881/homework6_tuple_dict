'hw_6.3'
number_input = input('Введіть ціле число: ')
number = int(number_input)

while number > 9:
    product = 1
    start_number = number
while start_number > 0:
    digit = number % 10
    product *= digit
    start_number //= 10
    start_number = product

    print(f'{number_input} -> {number}')
