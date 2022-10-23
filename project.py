import csv
data=[]
data2=[]
with open ('https://en.wikipedia.org/wiki/List_of_brown_dwarfs')as f:
    files=csv.reader(f)
    for y in files:
        data2.append(y)

with open ('archive_dataset.csv')as f:
    file=csv.reader(f)
    for i in file:
        data.append(i)
    
header1=data2[0]
brown_dwarf_data1=data2[1:]
header2=data[0]
brown_dwarf_data2=data[1:]
headers=header1+header2
brown_dwarf_data=[]

for index,data1 in enumerate(brown_dwarf_data1):
    brown_dwarf_data.append(brown_dwarf_data1[index]+brown_dwarf_data2[index])

with open ('class-129output.csv','a+')as file:
    reader=csv.writer(file)
    reader.writerow(headers)
    reader.writerows(brown_dwarf_data)