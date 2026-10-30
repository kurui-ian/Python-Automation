def greet(name):
    print("Hello "+name+". Hope your are doing great.")
    pass

greet("Kurui")
greet("Ian")

def check_temperature(temperature):
    if temperature >= 25:
        print("It is Hot outside. Dink alot of water")
    elif temperature > 0 and temperature < 25:
        print("It is cold outside. Wear warm clothes")
    else:
        print("Invalid temperature")

check_temperature(25)

#calculate total Price

def calculate_total(price):
    tax = price * 0.25
    discount = 1500
    total_pice = price + tax
    return total_pice

print(calculate_total(15000))


#calculating area

def calculate_area(height, width):
    return height * width

print(f"Area: {calculate_area(50,30)}")


