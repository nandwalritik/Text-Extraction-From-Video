import pytesseract
from PIL import Image
import json
import os
from tqdm import tqdm

my_dict = {}

# Loading frames from directory 
frames = os.listdir('./image_frames')

# Sorting frames according to their numbers
frames.sort(key=lambda x: int(x[5:-4]))

# printing total number of frames loaded
print("Number of frames :- " + str(len(frames)))

for frame in tqdm(frames):

    # extracting text from image frame
    text_in_image = pytesseract.image_to_string('./image_frames/'+frame)

    # replacing \n and \f character
    text_in_image = text_in_image.replace('\n', '')
    text_in_image = text_in_image.replace('\f', '')

    # Removing unwanted spaces
    text_in_image = text_in_image.strip()

    # removing unicode characters
    text_in_image = text_in_image.encode('ascii', 'ignore').decode()

    # appending output to dictionary (only those frames which contain text)
    if(len(text_in_image) != 0):        
        my_dict[str(frame)] = text_in_image

# print(my_dict)

# Saving output of dictionary to json file
with open('image_to_text.json', 'w') as outputFile:
    json.dump(my_dict, outputFile)
