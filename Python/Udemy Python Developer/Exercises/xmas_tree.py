#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
for row in picture: #iterate through each row
    for pixel in row:#iterate through each entry
        if pixel: #print * if 1
            print('*', end = '')
        else:#print empty if 0
            print(' ', end ='')
        
    print('') #if a row is finished, make a new line