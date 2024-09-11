import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
           'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_list = random.sample(letters, nr_letters)
symbol_list = random.sample(symbols, nr_symbols)
number_list = random.sample(numbers, nr_numbers)
easy_list = letter_list + symbol_list + number_list
hard_list = random.sample(easy_list, len(easy_list))
print(easy_list)
print(hard_list)

# passw = easy_list[0]
# for n in range(1, len(easy_list)):
#     passw += easy_list[n]
# print(passw)
#
# passw2 = hard_list[0]
# for n in range(1, len(hard_list)):
#     passw2 += hard_list[n]
# print(passw2)

passw = str()
for n in easy_list:
    passw += n
print(passw)

passw2 = str()
for n in range(len(hard_list)):
    passw2 += hard_list[n]
print(passw2)