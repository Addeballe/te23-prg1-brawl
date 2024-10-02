import random

#Namn och välkommanden
print ("Välkommen till mitt Den Stora Duellen! ")

spelare_ett_namn = input("Skriv in namnet för spelare ett:")
spelare_två_namn = input("Skriv in namnet för spelare två:")
#spelare_ett_klass = input("Skirv in klass för spelare ett ():")

#spelvariabler
spelare_ett_liv = 10
spelare_två_liv = 10
rundantal = 1
combat_hit = ['magen', 'armen', 'huvudet', 'benet']
player_one_trött = True
player_two_trött = True
player_one_sista = True
Player_two_sista = True
#spelvariabler

print (f"{spelare_ett_namn} och {spelare_två_namn} står mot varandra i arenan. Den med som först tar ned sin motståndare vinner! Må den bästa krigaren vinna!")
spel_aktivitet = input("Starta Duellen?(Y/N)")

if spel_aktivitet == "N":
    print("Men varför är du ens här då? Fegis..")

#combat
while True:
    spelare_ett_attack = random.randint(1,20)
    spelare_två_attack = random.randint(1,20)
    
    
    
    if spelare_ett_attack >= spelare_två_attack:
        spelare_två_liv -= 1
        print(f"{spelare_ett_namn} lyckas slå till {spelare_två_namn} i {random.choice(combat_hit)}!")
    elif spelare_två_attack >= spelare_ett_attack:
        spelare_ett_liv -= 1
        print(f"{spelare_två_namn} lyckas slå till {spelare_ett_namn} i {random.choice(combat_hit)}!")
    else:
        print("Ingen lyckas slå till varandra!")


#fixa detta
        if spelare_ett_liv == 5 and player_one_trött is True:
            print(f"{spelare_ett_namn} börjar att bli trött!")
            player_one_trött = False

        elif spelare_två_liv == 5 and player_two_trött is True:
            print(f"{spelare_två_namn} börjar att bli trött!")
            player_two_trött = False

        elif spelare_ett_liv == 2 and player_one_sista is True:
            print(f"{spelare_ett_namn} står på sina sista ben!")
            player_one_sista = False

        elif spelare_två_liv == 2 and player_two_sista is True:
            print(f"{spelare_två_namn} står på sina sista ben!")
            Player_two_sista = False
    
    
    
    if spelare_ett_liv == 0 or spelare_två_liv == 0:
       break