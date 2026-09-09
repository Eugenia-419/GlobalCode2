
# # product = input("Enter the product name: ")
# # price = float(input("Enter the price of the product: "))
# # quantity = int(input("Enter the quantity of the product: "))

# # total = price * quantity

# # print(
# #     f"The item you bought is {product}, the price for your item is {price}, and the quantity is {quantity} and the everything sums to {total}")
# # print("===================================")
# # print("           RECEIPT                ")
# # print("===================================")
# # print("Product: " , product)
# # print("Quantity: " , quantity)
# # print("Price: " , price)
# # print("Total: " , total)

# age = int(input("Enter your age: "))
# if age >= 18:
#     print ("You are eligible to vote.")
# else: 
#     print ("You are not eligible to vote.")

# light = input("Enter any color of your choice: ")
# if light == "Red" or "RED" or "red":
#     print("Stop")
# elif light == "Yellow" or "YELLOW" or "yellow":
#     print("Get ready")
# elif light == "Green" or "GREEN" or "green":
#     print("Go.....")

# score = int(input("Enter your score here: "))

# if score >= 85:
#     print("A")
# elif score >= 75:
#     print("B")
# elif score >= 65:
#     print("C")
# elif score >= 55:
#     print("D")
# elif score >= 45:
#     print("E")
# elif score >= 40:
#     print("F")
# else:
#     print("FAIL")


username = input("Enter your username: ")
password = input("Enter your password: ")
users = {
    'admin1': 'password1',
    'admin2': 'password2',
    'admin3': 'password3'
}

if users [username] ==  password:
    print("Login successful.")
else:
    print("Login failed.")
