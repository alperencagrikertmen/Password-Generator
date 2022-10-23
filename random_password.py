#Password Generator Project

# Avaliable Characters
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Prompts
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creating a random character
random_letter = random.randint(0, len(letters)-1)
random_number = random.randint(0, len(numbers)-1)
random_symbols = random.randint(0, len(symbols)-1)

length_of_password = nr_letters + nr_numbers + nr_symbols

password = []
  
#Creting a list of random characters
for letter in range(1, nr_letters+1):
  random_letter = random.randint(0, len(letters)-1)
  created_letter = letters[random_letter]
  password.append(created_letter)

for number in range(1, nr_numbers+1):
  random_number = random.randint(0, len(numbers)-1)
  created_number = numbers[random_number]
  password.append(created_number)

for symbol in range(1, nr_symbols+1):
  random_symbol = random.randint(0, len(symbols)-1)
  created_symbol = symbols[random_symbol]
  password.append(created_symbol)
 
#Shuffling the list
random.shuffle(password)

#Creating a string variable for password display
str_password = ""
for i in password:
  str_password = str_password + i

print(f"Your password is: {str_password}")