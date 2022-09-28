import pandas as pd
import glob,os

l=[]
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
#The 5 Choices you have
print("Choose from 1 to 5\n1. Create Open Script\n2. Create Send Bids Script\n3. Create Mix and Match\n4. Create None Script\n5. Exit")
choice=input("")
#You will repeat entering the choice until you choose a number between 1 and 5
while choice not in ["1","2","3","4","5"]:
    choice=input("Choose a number between 1 and 5:")
# if you choose 5 the program exit
if choice=="5":
    quit()
#Here you choose how many names you want for the output files
number=input("How many names you want:")
#Now we create a list that contains the values that we will use depends on the first choice
if choice=="1":
    df=data.loc[data["Action"]=="Open"]
    newList=list([df["Action"].tolist(),df["Name"].tolist()])
elif choice=="2":
    df=data.loc[data["Action"]=="Bid"]
    newList=list([df["Action"].tolist(),df["Name"].tolist(),df["Bid"].tolist(),df["Blind"].tolist()])
elif choice=="3":
    df=data.loc[data["Action"]=="Redeem"]
    newList=list([df["Action"].tolist(),df["Name"].tolist()])
elif choice=="4":
    df=data.loc[data["Action"]=="None"]
    newList=list([df["Action"].tolist(),df["Name"].tolist()])
#we transform the old list into a new one with the right syntax
for i in range(len(newList[0])):
    if len(newList)==2:
        l.append([newList[0][i],newList[1][i]])
    elif len(newList)==4:
        l.append([newList[0][i],newList[1][i],newList[2][i],newList[3][i]])
#You enter the neame of the output files, if you forgot to add the extension the program will add .txt
nameOfFile=input("enter the name of the output file:")
if nameOfFile.endswith(".txt")==0:
    nameOfFile+=".txt"
z=0
#if you have more than one files we iterate it's names
for i in range (0,len(l),int(number)):
    f=open(nameOfFile.split(".")[0]+str(z)+"."+nameOfFile.split(".")[1],"w")
    f.write("hsw-rpc sendbatch '" + str(l[i:i+int(number)]) + "'")
    f.close()
    z+=1
