file=open("names.txt","w")
file.write("mohammed,Ali,Hussain,Hassan,Ahmed")
file.close()

with open("names.txt","r") as name:
    print(name.read())