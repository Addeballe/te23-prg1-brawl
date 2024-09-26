#Namn och välkommanden
print ("Välkommen till mitt Den Stora Duellen! ")

spelare_ett_namn = input("Skriv in namnet för spelare ett:")
spelare_två_namn = input("Skriv in namnet för spelare två:")
#spelare_ett_klass = input("Skirv in klass för spelare ett (krigare, helare, tjuv):")

#spelvariabler
spelare_ett_liv = 10
spelare_två_liv = 10

rundantal = 1

from random import randint

print (f"{spelare_ett_namn} och {spelare_två_namn} är i en duell mot varandra. Den med som först tar ned sin motståndare vinner. Må den bästa vinna!")
spel_aktivitet = input("Starta Duellen?(Y/N)")

if spel_aktivitet == "N":
    print("Men varför är du ens här då?")



while True:
    
    

    if spelare_ett_liv == 0 or spelare_två_liv == 0:
        break