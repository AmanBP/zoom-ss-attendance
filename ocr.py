from PIL import Image
import pytesseract
import os
from location import location

image_dir = input("Enter Image Directory(Press enter to use default directory(if set in location.py)):")
if(len(image_dir)<1):
    image_dir = location
os.chdir(image_dir)
print("!!!ENSURE IMAGES ARE NUMBERED from 1 and are jpegs!!!")
limit = int(input("Enter Number of images:"))
im = [None]*limit
for i in range(limit):
    im[i] = Image.open("{}.jpeg".format(i+1))
for i in range(limit):
    iw, ih = im[i].size
    left = 75
    top = 0
    bottom = ih
    right = iw-120
    im[i] = im[i].crop((left,top,right,bottom))
final_str = pytesseract.image_to_string(im[0],lang="eng")
for i in range(1,limit):
    final_str = final_str + "\n" + pytesseract.image_to_string(im[i],lang="eng")
#print(final_str)

values = final_str.split(" ")
values2 = []
for val in values:
    if(val):
        if("\n" in val):
            v = val.split("\n")
            for i in v:
                if(i):
                    if("-" in i):
                        isplit = i.split("-")
                        for j in isplit:
                            if(j):
                                values2.append(j)
                    else:
                        values2.append(i)
        else:
            values2.append(val)

if(input("Clean Through the data?(Only for AIML) (y/n):") != 'n'):
    #print("Initial\n",values2)
    index = 0
    for i in range(0,len(values2)):
        if(values2[i] == "Priyadharsini-"):
            index = i-2
            break
    for i in range(4):
        values2.pop(index)
    values2.insert(len(values2),"RA1811026020009")
    #print("\n\nDeleting 9's BS\n",values2)
    for i in range(0,len(values2)):
        if(values2[i] == "1811026020059"):
            index = i-1
    for i in range(2):
        values2.pop(index)
    values2.insert(len(values2),"RA1811026020059")
    #print("\n\nDeleting 59's BS\n",values2)
    for i in range(0,len(values2)):
        if(values2[i] == "RA1811026020058_"):
            index = i
    for i in range(1):
        values2.pop(index)
    values2.insert(len(values2),"RA1811026020058")
    #print("Deleted 58's BS\n",values2)

rolls = []
for i in range(len(values2)):
    if(values2[i].startswith("RA")):
        rolls.append(int(values2[i][len(values2[i])-2:]))
    if(values2[i].isnumeric()):
        rolls.append(int(values2[i]))
print("\n\nEnsure to Cross-Check!\nAttendance:")
print(sorted(rolls))