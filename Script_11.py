
#Fonction pour enlever les espaces
CH="  Salut tout le monde  "
print(len(CH))
print(CH.strip())
#print(len(CH.strip()))

#la chaine de caractère n'est pas modifiable (voir l'enregistrement 1:33)
CH1=CH.strip()
print(CH1)
print(len(CH1))
#enlever les espace avant avec la fonction lstrip
CH1=CH.lstrip()
print(CH1)
print(len(CH1))
#enlever les espace après avec la fonction rstrip
CH1=CH.rstrip()
print(CH1)
print(len(CH1))
ch4="***salut***tout***le***monde***"
print(ch4)
ch5=ch4.strip("*")
print(ch5)
print(len(ch5))
# remplacer l'étoile avec l'espace
print(ch5.replace("*"," "))

print(ch5.replace("*",""))
#pour changer la casse
CH6=" SALUT Tout le monde  "
print(CH6.lower())
print(CH6.upper())
#afficher le nombre des mots qui se répète
ch7=" Salut tout le monde  le monde "
print(ch7.count("monde"))
#pour commencer ou afficher un mot dans la chaine de caractére ça retourne true ou false
print(ch7.startswith(" Salut"))
print(ch7.endswith("Salut"))
# la fonction split
ch8="un-deux-trois-quatre-cinq"
print(ch8.split("-"))