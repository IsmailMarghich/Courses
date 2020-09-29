def computepay(h,r): #compute your houlry wage with a 1.5 multiplier after 40 hours
    float(h)
    float(r)
    z = r * 1.5
    if h > 40:
        return 40 * r + (h - 40) * z 
    else:
       return h * r


print(computepay(45, 10.50))