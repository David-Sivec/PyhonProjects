calculation = input("Enter a quation like this 'number1' 'operator' 'number2': ")
try:
  number1 = float(calculation[0])
  operator = calculation[2]
  number2 = float(calculation[4])
  if operator == "+":
    result = number1 + number2
  elif operator== "-":
    result = number1 - number2
  elif operator == "*":
    result = number1 * number2
  elif operator == "/":
    if number2 == 0:
      result = "Error: Division by zero is not allowed."
    else:
      result = number1 / number2
  else:
    result = "Error: Invalid operator. Use +, -, *, or /."
  print(f"The result of {calculation} is: {result}")
except (ValueError, IndexError):
  print("Error: Please enter a valid calculation in the format 'number1 operator number2'.")