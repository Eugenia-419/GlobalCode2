# def hello():
#     print("Hello")
# hello()

# def goodbye():
#     print("Goodbye")
# goodbye()

# def nameSchool():
#     print("HTU")
# nameSchool()
# num1 = 0
# num2 = 0
# def add(num1 , num2):
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     print(f"the sum of {num1} and {num2} is {num1 + num2}")
# add(num1 ,num2)               

def light(color):
    if color == "Red" or color == "RED" or color == "red":
        print("Stop")
    elif color == "Yellow" or color == "YELLOW" or color == "yellow":
        print("Get ready")
    elif color == "Green" or color == "GREEN" or color == "green":
        print("Go.....")
    else:
        print("Invalid Color")
color = input("Enter any color of your choice: ")
light(color)



s