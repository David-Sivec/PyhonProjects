main_input = int(input("Co chcete previest (1 - cm - inch/inch - cm, 2 - farnheit - celsius/celsius - farnheit): "))
if main_input == 1:
  cm_inch = input("zadaj jednotku (cm alebo inch): ")
  if cm_inch == "cm":
    cm = float(input("zadaj dlzku v centimetroch: "))
    vzorec3 = cm // 2.54
    print("Dlzka v palcoch je: ", vzorec3)
  elif cm_inch == "inch":
    inch = float(input("zadaj dlzku v palcoch: "))
    vzorec4 = inch * 2.54
    print("Dlzka v centimetroch je: ", vzorec4)
  else:
    print("Zadali ste nespravnu jednotku. Zadajte 'cm' alebo 'inch'.")
elif main_input == 2:
  far_cel = input("zadaj jednotku (F alebo C): ")
  if far_cel == "F":
    far = float(input("zadaj teplotu vo Fahrenheitoch: "))
    vzorec1 = (far - 32) * 5 // 9
    print("Teplota vo stupnoch Celzia je: ", vzorec1)
  elif far_cel == "C":
    cel = float(input("zadaj teplotu vo stupnoch Celzia: "))
    vzorec2 = (cel * 9 / 5) + 32
    print("Teplota vo Fahrenheitoch je: ", vzorec2)
  else:
    print("Zadali ste nespravnu jednotku. Zadajte 'F' alebo 'C'.")
else:
  print("Zadali ste nespravnu moznost. Zadajte '1' alebo '2'.")
