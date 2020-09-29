text = "X-DSPAM-Confidence:    0.8475"; #find and slice the string so we only have the numbers
x = text.find(':') #find the location of the :
print(float((text[x+1:]))) #print the float numbers after but not including the :