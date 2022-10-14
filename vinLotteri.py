import random
print("Ikke la sigurd kjøre, han er QA og kræsjer programmer")
print("Skriv inn navn og sum per person: eksempel for Sigud så han klarer å kjøre programmet \n Eksempel: Martin 100\n")
word = ""
liste = []
while True:
    lal = input().split()
    if(lal[0] == "stop"):
        break
    elif (lal.__len__() < 2 or lal.__len__() > 2):
        continue
    elif(int(lal[1]) % 25 == 0):
        lodd = int(int(lal[1])/25)
        for x in range(lodd):
            liste.append(lal[0])
        word = lal[0]
print("\n")
random.shuffle(liste)
print(*liste, sep="\n")

#kjempefin kode :)
#Created by: Elias Helgeland ;)
