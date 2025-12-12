print("Wellcome Bill System")

#pizza list
small_pizza=100
medium_pizza=150
large_pizza=250

#add pepper
add_pepper_small_pizza=20
add_pepper_medium_or_large_pizza=50

#add cheese
add_chesse_pizza=60

#start bill rate
bill=0

#User input
size=input("Enter your pizza size like [ S / M / L ] ")
add_pepper=input("Enter your pizza Pepper like [ Y / N ] ")
add_cheese=input("Enter your pizza Cheese like [ Y / N ] ")

#control flow for pizza size
if size=="S":
    bill+=small_pizza
elif size=="M":
     bill+=medium_pizza
elif size=="L":
     bill+=large_pizza
else:
     print("Invilade option")

#control flow for add pepper
if add_pepper=="Y":
     if size=="S":
          bill+=add_pepper_small_pizza
     elif size=="M":
          bill+=add_pepper_medium_or_large_pizza
     elif size=="L":
          bill+=add_pepper_medium_or_large_pizza
else:
     print("Invilade option for pepper")

#control flow for add cheese
if add_cheese=="Y":
     bill+=add_chesse_pizza

print(f"Thankyou for buying my store your price is :> {bill}")
     
  
