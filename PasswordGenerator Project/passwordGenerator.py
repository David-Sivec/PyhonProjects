import random

character_count = random.randint(8, 12)
password_characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j","K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = ""
for i in range(character_count):
  random_character = random.choice(password_characters)
  password += random_character

print(password)