import graphics

def add(n1, n2):
  return n1 + num2

def subtract(n1, n2):
  return n1 - n2


def multiply(n1,n2):
  return n1 * n2

def divide(n1, n2):

  if n2 != 0:
    return n1 / n2
  else:
    return None

print(graphics.logo)

def calculator():
  should_continue = True

  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

  num1 = float(input("What is the first number? "))

  while should_continue:

   
    for operator in operations:
      print(operator)

    operation = input("Pick an operation: ")
    num2 = float(input("What is the next number? "))

    answer = operations[operation](num1,num2)

    print(f"{num1} {operation} {num2} = {answer}")
     
    if input("Type 'y' to continue {answer}, or type 'n' to start a new calculation:") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
 

calculator()

    

