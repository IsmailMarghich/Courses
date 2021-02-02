#this file showcases a few ways we can stop our program from breaking when an error occurs
while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError: #if you write the wrong type instead of integer or float
        print('please enter a number')
        continue
    except ZeroDivisionError: #if you enter a zero, which is an invalid age. this will divide by zero as a check
        print('please enter age higher than 0')
        continue
    else:
        print('thank you') #if none of these errors occured, continue
