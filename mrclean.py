

import pandas as pd       
from bs4 import BeautifulSoup
import numpy as np
import csv

words = []
with open('urban.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count=0
    string=""
    for row in readCSV:
        count+=1
        if count > 100:
            break
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
        
        if len(description)>2 and term.find("/")==-1:
            words.append("%s: %s \n"%(term,description))

file=open("input.txt","w")
for word in words:
    file.write(word)
file.close()

