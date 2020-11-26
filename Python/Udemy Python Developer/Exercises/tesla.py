#make a function called checkDriverAge() that takes
#an age input and outputs wether u can drive or not
def checkDriverAge(age=0): #define default age at 0
    if int(age) < 18: 
        print('you are too young to drive')
    elif int(age) > 18:
        print('you are old enough to drive')
    elif int(age) == 18:
        print('enjoy your first year of driving')
checkDriverAge(17)
checkDriverAge(18)
checkDriverAge(19)