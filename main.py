import pandas as pd
import glob,os,re
#You enter the path of the file
path = '.'
extension = 'csv'
#os.chdir(path)
result = glob.glob('*.{}'.format(extension))
count = 1
for res in result:
    print(count,". ",res)
    count += 1
print("please choose the correct no")
fileInput=input("Enter file no:")
data = pd.read_csv(result[int(fileInput) - 1])
#print(data)
print(type(data))
tu = data.values.tolist()
print(tu[:5])
#tu = input("this")

l=[]
for u in tu:
    temp = []
    g = u[1]
    g = g.upper()
    temp.append(g)
    w = u[0]
    w = w.lower()
    temp.append(w)
    if(g == "BID"):
        temp.append(u[2])
        temp.append(u[3])
    l.append(temp)
#Here you choose how many names you want for the output files
number=input("How many names you want in a single file :")
#You enter the neame of the output files, if you forgot to add the extension the program will add .txt
#nameOfFile=input("enter the name of the output file:")
nameOfFile = "output"
if nameOfFile.endswith(".txt")==0:
    nameOfFile+=".txt"
z=0
#if you have more than one files we iterate it's names
for i in range (0,len(l),int(number)):
    f=open(nameOfFile.split(".")[0]+str(z)+"."+nameOfFile.split(".")[1],"w")
    jk = str(l[i:i+int(number)])
    jk = re.sub("\'",'"',jk)
    f.write("hsw-rpc sendbatch '" + jk + "'")
    f.close()
    z+=1
