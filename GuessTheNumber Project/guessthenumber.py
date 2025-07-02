import random

computer_number = random.randint(1, 50)
print(computer_number)
user_guess = 0

while user_guess != 10:
  input_number = int(input("hadaj cislo od 1 do 50: "))
  if input_number < computer_number:
    user_guess += 1
    print("Zadali ste mensie cislo ako je tajne cislo.")
    print("Pocet zostavaajucich pokusov", 10 - user_guess)
  elif input_number> computer_number:
    user_guess += 1
    print("Zadali ste vacsie cislo ako je tajne cislo.")
    print("Pocet zostavaajucich pokusov", 10 - user_guess)
  else:
    user_guess += 1
    print("Gratulujem, uhadol si tajne cislo!")
    print("pocet pokusov: ", user_guess)
    break
  if user_guess == 10:
    print("Koniec hry, skus to nabuduce.")
    print("Tajne cislo bolo: ", computer_number)
    break