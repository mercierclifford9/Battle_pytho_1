import re
x=input("Antre on fraz\n")
y=[]
for i in x:
    dijitt=re.findall(r'\d+', x)
    dijitt=[int(dijit) for dijit in dijitt]

print("dijit yo se :")
for i in dijitt:
    print(i)
nb_val=len(dijitt)
print("kantite dijit yo se :" + str(nb_val))
