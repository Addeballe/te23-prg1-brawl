import random

#-----------------------------------------------Game Variables---------------------------------
spelare_ett_liv = 100
spelare_två_liv = 100

combat_hit = ['magen', 'armen', 'huvudet', 'benet']

player_one_trött = True
player_two_trött = True
player_one_sista = True
player_two_sista = True

vapen = ['spikklubba', 'spjut', 'långsvärd', 'kortsvärd', 'dolk', 'inget vapen/händer']
skydd = ['ringbrynja', 'plåtrustning', 'läder', 'naken']
sekundär = ['sköld', 'parrydolk', 'mini-armborst']

player_one_attack = 0
player_one_defence = 0
player_one_movement = 0

player_two_attack = 0
player_two_defence = 0
player_two_movement = 0
#-------------------------------------------------------------------------------------------------

print ("Välkommen till mitt Den Stora Duellen! ")
spelare_ett_namn = input("Skriv in namnet för krigare ett:")
spelare_två_namn = input("Skriv in namnet för krigare två:")
print (f"{spelare_ett_namn} och {spelare_två_namn} möter varandra i arenan. Den med som först tar ned sin motståndare vinner! Må den bästa krigaren vinna!")
spel_aktivitet = input("Starta Duellen?(Y/N)")



if spel_aktivitet == "N":
    print("Men varför är du ens här då? Fegis..")



print("Den lokala smeden går ut på arenan. ")



while True: 
    if spel_aktivitet == "N":
        break

    spelare_ett_combatroll = random.randint(1,20)
    spelare_två_combatroll = random.randint(1,20)
    
    if spelare_ett_combatroll > spelare_två_attack:
        spelare_två_liv -= 1
        print(f"{spelare_ett_namn} lyckas slå till {spelare_två_namn} i {random.choice(combat_hit)}!")
    elif spelare_två_attack > spelare_ett_attack:
        spelare_ett_liv -= 1
        print(f"{spelare_två_namn} lyckas slå till {spelare_ett_namn} i {random.choice(combat_hit)}!")
    else:
        print("Ingen lyckas slå till varandra!")


    if spelare_ett_liv <= 50 and player_one_trött is True:
        print(f"{spelare_ett_namn} börjar att bli trött!")
        player_one_trött = False

    elif spelare_två_liv <= 50 and player_two_trött is True:
        print(f"{spelare_två_namn} börjar att bli trött!")
        player_two_trött = False

    elif spelare_ett_liv <= 20 and player_one_sista is True:
        print(f"{spelare_ett_namn} står på sina sista ben!")
        player_one_sista = False

    elif spelare_två_liv <= 20 and player_two_sista is True:
        print(f"{spelare_två_namn} står på sina sista ben!")
        Player_two_sista = False

    if spelare_ett_liv == 0 or spelare_två_liv == 0:
       if spelare_ett_liv 
       