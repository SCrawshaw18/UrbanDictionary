
# coding: utf-8

# In[11]:


import csv
import json
words = []

bads=open("en.txt","r")
listbads=bads.read().split("\n")
print(listbads)
with open('urban.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count=0
    for row in readCSV:
        if len(row)==6:
            if count % 10000 == 0:
                print(str(count))
            description = row[5]
            if description.find(";") != -1:
                description = description[:description.find(";")]
            description=description.replace("1.","")
            description=description.replace("1 ","")
            description=description.strip()
            description=' '.join(description.split())
            description=description.replace(" ,",",")
            description=description.replace("\n","")
            
            term=row[1].lower()
            mean=False
            for bad in listbads:
                if bad.lower() in term.lower() or bad.lower() in description.lower():
                    mean=True
            if len(description)>2 and term.find("/")==-1 and count % 25 == 0 and not mean:
                words.append("%s: %s \n"%(term,description))
    print(words)
file=open("input.txt","w")
for word in words:
    file.write(word)
file.close()

