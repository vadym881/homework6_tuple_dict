'hw_6.1'
import string

user_input = input('Enter: ')
start_char, end_char = user_input.split('-')
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char) + 1

result = string.ascii_letters[start_index:end_index]
print(result)