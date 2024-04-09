debugMode = False
inventorySystem = []

try:
  f = open("inventorySystem.txt", "r")
  pizzaOrder = eval(f.read())
  f.close()
except:
  print("ERROR: Unable to load")
  if debugMode:
    print(traceback)

while True: 
  print("\nINVENTORY")
  print("=========")
  print()
  print("1: Add  2: View Item 3: View All  4: Remove")
  print()
  menu = input("> ")
  if menu == "1":
    addItem = input("What item would you like to add? ")
    inventorySystem.append(addItem)
  elif menu == "2":
    viewItem = input("What item would you like to view? ")
    if viewItem in inventorySystem:
      print(f"You have {inventorySystem.count(viewItem)} {viewItem}")
    else:
      print("You don't have that item.")
  elif menu == "3":
    for item in inventorySystem:
      print(item)
  elif menu == "4":
    removeItem = input("What item would you like to remove? ")
    if removeItem in inventorySystem:
      inventorySystem.remove(removeItem)
    else:
      print("You don't have that item.")
  else:
    print("Invalid input.")
    
  f = open("inventorySystem.txt", "w")
  f.write(str(inventorySystem))
  f.close()
  