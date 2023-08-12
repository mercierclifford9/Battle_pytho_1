import re
x=input("Antre on fraz\n")
y=[]
for i in x:
    dijitt=re.findall(r'\d+', x)
    dijitt=[int(dijit) for dijit in dijitt]
h=""
print("dijit yo se :")
for i in dijitt:
    h=h+str(i)
nb_val=len(h)
print(h)
print("kantite dijit yo se :" + str(nb_val))
print()
