import time
import random

# global variables
food = []
food_name = []
total = 0
count = 0

def hotel():
    print("        ***********  Hotel Management Swiggy  ***********      ")
    print("List of Hotels")
    print(" 1.Ambur Star Briyani")
    print(" 2.Dindigul Thalappakatti")
    print(" 3.Salem RR Briyani")
    print(" 4.A2B Restaurant")
    print(" 5.Exit")
    hotel_num = int(input(" Enter the Hotel Number: "))

    if hotel_num == 1:
        ambur()
    elif hotel_num == 2:
        dindigul()
    elif hotel_num == 3:
        salem()
    elif hotel_num == 4:
        a2b()
    elif hotel_num == 5:
        exit_app()
    else:
        print("Enter correct option")
        hotel()

# ---------------- Ambur Hotel ----------------

def ambur():
    cb = 180
    mb = 350
    c65 = 120

    print("\nWelcome to Ambur Star Briyani")
    print("1.Chicken Briyani ->", cb)
    print("2.Mutton Briyani  ->", mb)
    print("3.Chicken 65      ->", c65)
    print("4.Exit")

    food_num = int(input("Enter Food Number: "))

    if food_num == 1:
        add_food("Chicken Briyani", cb, ambur)
    elif food_num == 2:
        add_food("Mutton Briyani", mb, ambur)
    elif food_num == 3:
        add_food("Chicken 65", c65, ambur)
    elif food_num == 4:
        reset_cart()
        hotel()
    else:
        ambur()

# ---------------- Dindigul Hotel ----------------

def dindigul():
    cb = 200
    mb = 380
    grill = 120

    print("\nWelcome to Dindigul Thalappakatti")
    print("1.Chicken Briyani ->", cb)
    print("2.Mutton Briyani  ->", mb)
    print("3.Grill           ->", grill)
    print("4.Exit")

    food_num = int(input("Enter Food Number: "))

    if food_num == 1:
        add_food("Chicken Briyani", cb, dindigul)
    elif food_num == 2:
        add_food("Mutton Briyani", mb, dindigul)
    elif food_num == 3:
        add_food("Grill", grill, dindigul)
    elif food_num == 4:
        reset_cart()
        hotel()
    else:
        dindigul()

# ---------------- Salem Hotel ----------------

def salem():
    cb = 220
    mb = 400
    parota = 50

    print("\nWelcome to Salem RR Briyani")
    print("1.Chicken Briyani ->", cb)
    print("2.Mutton Briyani  ->", mb)
    print("3.Parotta         ->", parota)
    print("4.Exit")

    food_num = int(input("Enter Food Number: "))

    if food_num == 1:
        add_food("Chicken Briyani", cb, salem)
    elif food_num == 2:
        add_food("Mutton Briyani", mb, salem)
    elif food_num == 3:
        add_food("Parotta", parota, salem)
    elif food_num == 4:
        reset_cart()
        hotel()
    else:
        salem()

# ---------------- A2B ----------------

def a2b():
    meals = 150
    curd = 100
    lemon = 80

    print("\nWelcome to A2B")
    print("1.Meals      ->", meals)
    print("2.Curd Rice  ->", curd)
    print("3.Lemon Rice ->", lemon)
    print("4.Exit")

    food_num = int(input("Enter Food Number: "))

    if food_num == 1:
        add_food("Meals", meals, a2b)
    elif food_num == 2:
        add_food("Curd Rice", curd, a2b)
    elif food_num == 3:
        add_food("Lemon Rice", lemon, a2b)
    elif food_num == 4:
        reset_cart()
        hotel()
    else:
        a2b()

# ---------------- Common Functions ----------------

def add_food(name, price, hotel_func):
    qty = int(input("Enter Quantity: "))
    amount = price * qty
    food.append(amount)
    food_name.append(f"{name:<20} {price:<8} {qty:<8} {amount}")
    print(name, "Added")

    another = input("Add another dish? (yes/no): ").lower()
    if another == "yes":
        hotel_func()
    else:
        cart()

def cart():
    global total
    total = 0
    print("\n----------------------------------------------------")
    print("Food Name             Price   Qty     Total")
    print("----------------------------------------------------")
    for item in food_name:
        print(item)
    for amt in food:
        total += amt
    print("----------------------------------------------------")
    print("Total Amount:", total)
    payment()

def payment():
    print("\nPayment Methods")
    print("1.Gpay  2.Paytm  3.Phonepe  4.Exit")
    pay = int(input("Choose Payment: "))

    if pay in [1, 2, 3]:
        amount = int(input("Enter Amount: "))
        if amount == total:
            print("Processing Payment...")
            time.sleep(3)
            otp()
        else:
            print("Wrong Amount")
            payment()
    elif pay == 4:
        hotel()
    else:
        payment()

def otp():
    global otp_value
    otp_value = random.randint(1000, 9999)
    otp_check()

def otp_check():
    global count
    print("OTP:", otp_value)
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp_value:
        print("Order Confirmed ✅")
        print("Thank You! Visit Again")
    else:
        count += 1
        if count > 2:
            payment()
        else:
            print("Wrong OTP")
            otp_check()

def reset_cart():
    food.clear()
    food_name.clear()

def exit_app():
    print("Thank You..! Visit Again..!")

# ---------------- Start Program ----------------
hotel()
