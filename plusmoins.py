import random 
entry = int(input('Entrez un chiffre :'))
number = random.randint(1,100)
while entry !=  number:
    print(("c'est moins", "c'est plus")[entry < number])
    entry = int(input('Essaye encore :'))
print("c'est ok, le chiffre à trouver était", number)

