import os
os.system("clear")
print("""

          - - - - - -            - - - - -           | |           
         /  - - - - -           /  - - -  \          | |
        /  /                   /   /    \  \         | |
       /  /                   /   /      \  \        | |
       |  |                  /   /        \  \       | |
       |  |                 /   /          \  \      | |
       |  |                /   /_ _ _ _ _ _ \  \     | |
       \  \               /   /              \  \    | |
        \  \             /   /_ _ _ _ _ _ _   \  \   | |
         \  \_ _ _ _ _  /   /                  \  \  | |_ _ _ _ _
          \_ _ _ _ _ _ /   /                    \  \ | _ _ _ _ _
""")
import time as t
x = "The answer is "
print("\33[1;32;40m===================================")
print("""Tools:Simple Calculator
Creator:Spider
Team:Termuxhackz society
credit goes to :AnonTemitayo(D34D 5L33P)
WhatsApp:09052863644 or 08052863644
github:https://github.com/spider863644
""")
print("====================================")
#THIS IS THE FIRST NUMBER
number1 = float(input("Enter a number: "))
#THIS ARE THE OPERATORS
print("""CHOOSE AN OPERATION
[1] +
[2] -
[3] *
[4] ÷
""")
operator = (input("Enter an operator: "))
#SECOND NUMBER
number2 = float(input("Enter a number: "))
print("CHECKING INPUT...")
t.sleep(5)
print ("CHECKING OPERATOR...")
t.sleep(3)
print("CALCULATING...")
t.sleep(1)
if operator == "+": 
  print(x, number1 + number2)
elif operator == "-":
  print(x, number1 - number2)
elif operator == "*":
  print(x, number1 * number2)
elif operator == "÷":
  print(x, number1 / number2)
else:
  print("Choose a valid operator!")
op = input("Do you want to continue using calculator? Y/N: ")
while op == "Y":
  if op == "Y":
    continue

   