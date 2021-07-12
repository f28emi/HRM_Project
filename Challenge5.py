# file=open("demo.txt","w")
# file.close()
file=open("demo.txt","r")
inside=file.read()
print(inside)
file.close()



file=open("demo.txt","a")
file.write("\nTechnopark,Trivandrum")
file.close()