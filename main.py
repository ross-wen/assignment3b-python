def getPizzaSize():
  pizzaSize = str(input("What size of Pizza do you want? Enter \"Large\" for a Large Pizza($6.00) and Enter \"Extra Large\" for a Extra Large Pizza($10.00)\n"))
  while True:
    if (pizzaSize == "Large") or (pizzaSize == "Extra Large"):
      return pizzaSize
    pizzaSize = str(input("Invalid Input. Enter \"Large\" for a Large Pizza($6.00) and Enter \"Extra Large\" for a Extra Large Pizza($10.00)\n"))

def getNumTopping():
  toppings = str(input("How many toppings do you want? Choose from 0 to 4.\n"))
  while True:
    if (toppings == "0") or (toppings == "1") or (toppings == "2") or (toppings == "3") or (toppings == "4"):
      return toppings
    toppings = input("Invalid Input. Choose from 0 to 4.\n")


def main():
  price = 0
  size = getPizzaSize()
  num = getNumTopping()
  if size == "Large":
    price = price + 6
  elif size == "Extra Large":
    price = price + 10
  if num == "1":
    price = price + 1
  elif num == "2":
    price = price + 1.75
  elif num == "3":
    price = price + 2.5
  elif num == "4":
    price = price + 3.35
    
  print(str(round(price*1.13,2))+"$")

main()