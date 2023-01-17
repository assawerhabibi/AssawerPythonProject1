# num = int(input("Entrez un nombre: "))

# if num % 2 == 0:
#     print(num, "est un nombre pair.")
#else:
   # print(num, "est un nombre impair.")


def pair(num):
    '''cette fonction permet de vérifier si le nombre est pair ou impair'''
    if num % 2 == 0:
     print(num, "est un nombre pair.")
    else:
     print(num, "est un nombre impair.")
pair(4)
pair(7)
print(pair.__doc__)
