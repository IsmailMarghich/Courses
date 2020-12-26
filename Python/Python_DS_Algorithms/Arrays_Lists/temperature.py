#we make a program where a user can add temperatures for each day, and then it will calculate the average temperature
#it should also be able to print how many days are above average temperature

numDays = int(input('how many days? '))
total = 0
temp = []
for i in range(numDays):
    temperature = int(input(f'for day {i+1} what is the temperature? '))
    temp.append(temperature)
    total += temperature

avg = round(total/numDays, 2)
print(f'average = {avg}')
above = 0
lst = []
days = []
for j in temp:
    if j > avg:
        lst.append(j)
        above+=1
print(f'{above} day(s) are above average temperature')
print(lst, ' are above average') #print which days are above average
for i in lst:
    j = temp.index(i)
    days.append(j)
print(days, ' are the days that are above average')