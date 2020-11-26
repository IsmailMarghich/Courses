from PIL import Image, ImageFilter
import sys
import os
#grab the input folder as the first argument and the output folder as second argument
input_folder = sys.argv[1]
output_folder = sys.argv[2]
#check if an output folder already exists, if it doesnt, make a new one
if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)
#loop through the input folder and convert the images to .png files
for filename in os.listdir(input_folder): #for each image in input folder
    img = Image.open(f'{input_folder}/{filename}')#open the images  
    clean_name = os.path.splitext(filename)[0] #split the image name so we remove the .jpg in the nsmr
    img.save(f'{output_folder}/{clean_name}.png', 'png')#save the converted img with a .png extension
