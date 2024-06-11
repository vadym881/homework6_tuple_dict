'hw_6.3'
number_input = input('Введіть ціле число: ')
output = 1

for digit in number_input:
    output *= int(digit)

while output > 9:
    next_output = 1
    for digit in str(output):
        next_output *= int(digit)
    output = next_output

print(f'{number_input} -> {output}')
