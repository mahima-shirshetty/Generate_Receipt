# calculate the total bill of ABC customer at a store

sum = 0
while(True):
    number = input("Enter the price or press 'q' to quit: \n")
    if (number!='q'):
        sum = sum + int(number)
    
    else:
        print(f"You Total Bill is {sum}")
        print("Thanks for visiting the store!")

        break