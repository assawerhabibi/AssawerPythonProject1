# comment faire l'indexation
str1="salut tout le monde"
#affichage de la lettre u
print(str1[3])
#affichage de la lettre s
print(str1[0])
#affichage de la  dernière lettre
print(str1[-1])
print(str1[-2])
print(len(str1))
print(str1[len(str1)-1])
# Découpage de chaine de caractères
print(str1[0:5])
print(str1[6:10])
#si on laisse vide il copie tout jusqu' a la fin
print(str1[0:])
# affichage de tout le monde
print(str1[6:19])
str2="sabacada"
# faire un saut avec le pas
print(str2[1::2])
print(str1[1::2])
print(str1[1::3])
# récupérer 6 caractères on spécifie pas le début
print(str1[:7])
# indexation à partir de la fin
print(str1[-4:])
#inverser la chaine
print(str1[::-1])
#concaténation
str3="Assawer"
str4="Habibi"
str5=str3+" "+str4
# différent type d'affichage
print(str3,str4)
print(str5)
print(str3+" "+str4)
str3=str3+str3
print(str3)
#si on veut afficher les carctére un par un
 # dans java on écrit comme ça :for(int i=0;i3++)`{}
 # dans python:
for i in str3:
    print(i)
