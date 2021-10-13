username = input("Please enter you first name! ")
number1 = input("Enter you favorite number! ")
try:
    number1 = int(number)
except:
    print("Okay! Processing")
    try:
        number1 = float(number)
    except:
        print("Just confirming your number....")
        
print(username + "\'s favorite number is " + number1)

