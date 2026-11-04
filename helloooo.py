def module(name,age,phone_number):
    choice = input((f"Hello {name}, you are {age} years old. Your phone number is {phone_number}. Are these details correct?"))
    if choice.lower() == "yes":
        print("Thank You for your time")
    else:
        print("Enter the details by yourself: /n")
        name = input("Name: ")
        age =  input("Age: ")
        phone_number = input("Phone Number: ")

        module(name,age,phone_number)


module("Kurui", 19, "074119242")

    