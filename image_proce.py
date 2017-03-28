import os, sys, getopt
from PIL import Image, ImageOps

# Parsing the arguments.
opts, args = getopt.getopt(sys.argv[1:], 'd:w:h:')
 
# Set some default values to the needed variables.
directory = ''
width = -1
height = -1
 
# If an argument was passed in, assign it to the correct variable.
for opt, arg in opts:
    if opt == '-d':
        directory = arg
    elif opt == '-w':
        width = int(arg)
    elif opt == '-h':
        height = int(arg)
 
# We have to make sure that all of the arguments were passed.
if width == -1 or height == -1 or directory == '':
    print('Invalid command line arguments. -d [directory] ' \
          '-w [width] -h [height] are required')
 
    # If an argument is missing exit the application.
    exit()
    

#Create output directory

out_dir = directory+'/resized/'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Iterate through every image given in the directory argument and resize it.
for image in os.listdir(directory):
    print('Resizing image ' + image)
 
    # Open the image file.
    img = Image.open(os.path.join(directory, image))
    
    #Equalize histogram
    img = ImageOps.equalize(img)
 
    # Resize it.
    img = img.resize((width, height), Image.BILINEAR)

    
 
    # Save it back to disk.
    img.save(os.path.join(out_dir, 'resized-'+ image))
 
print('Batch processing complete.')

