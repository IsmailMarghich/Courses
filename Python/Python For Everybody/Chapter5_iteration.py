largest = None #declaring default values
smallest = None
while True: #loop
    try: #try to run the whole code with an int converson
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest is None or largest < num: #checking for the largest
            largest = num
        elif smallest is None or smallest > num: #checking for the smallest
             smallest = num
    except ValueError: #if its an invalid input, restart loop
        print("Invalid input")
        continue

print ("Maximum is", largest)
print ("Minimum is", smallest)