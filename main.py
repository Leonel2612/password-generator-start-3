#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pos_letters=0
n_letter=0

list_letter=""
pos_letter=len(letters)
for n_letter in range(0, nr_letters):
  r_letters=random.randint(0,pos_letter-1)
  position_letter=letters[r_letters]
  list_letter+=position_letter
#print(list_letter)
##
pos_letters=0
n_symbol=0
list_symbol=''
pos_symbol=len(symbols)
for n_symbol in range(0, nr_symbols):
  r_symbols=random.randint(0,pos_symbol-1)
  position_symbol=symbols[r_symbols]
  list_symbol+=position_symbol
#print(list_symbol)

##
n_numbers=0
list_numbers=''
pos_numbers=len(numbers)
for n_numbers in range(0, nr_numbers):
  r_numbers=random.randint(0,pos_numbers-1)
  position_numbers=numbers[r_numbers]
  list_numbers+=position_numbers
#print(list_numbers)

con_final=list_letter+list_symbol+list_numbers


print(f'Your password final is\n{con_final}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print ('\n')

list_letter2=[]
pos_letter2=len(letters)
for n_letter2 in range(0, nr_letters):
  r_letters2=random.randint(0,pos_letter2-1)
  position_letter2=letters[r_letters2]
  list_letter2.append(position_letter2)
#print(list_letter)
##

n_symbol2=0
list_symbol2=[]
pos_symbol2=len(symbols)
for n_symbol2 in range(0, nr_symbols):
  r_symbols2=random.randint(0,pos_symbol2-1)
  position_symbol2=symbols[r_symbols2]
  list_symbol2.append(position_symbol2)
#print(list_symbol)

##
n_numbers2=0
list_numbers2=[]
pos_numbers2=len(numbers)
for n_numbers in range(0, nr_numbers):
  r_numbers2=random.randint(0,pos_numbers-1)
  position_numbers2=numbers[r_numbers2]
  list_numbers2.append(position_numbers2)
#print(list_numbers)

con_final2=list_letter2+list_symbol2+list_numbers2

#print(con_final2)

random.shuffle(con_final2)

#print(con_final2)

password_shuffle=''
for final_s in con_final2:
  password_shuffle+=final_s


print(f'Your password final is\n{password_shuffle}')
