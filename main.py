print("Welcome to Abishek Coffee")

print("This Cafa Prices is Fixed Price Like 499")
name = input("Enter Your Name: ")
print("Select Menu List")

menu=("""1.Black coffee
2.espresso
3.Latte
4.Cappucino""")

print(menu)
output = input("Enter Like [ 1 / 2 / 3 / 4 ]: ")
price = 499
quantity = input("How many coffee did you want: ")
total = price * int(quantity)
print("Thankyou for buying your total price is >"+str(total))