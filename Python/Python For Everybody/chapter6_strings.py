text = "X-DSPAM-Confidence:    0.8475";
x = text.find(':')
print(float((text[x+1:])))