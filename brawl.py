import random



#-----------------------------------------------Game Variables---------------------------------
spelare_ett_liv = 50
spelare_två_liv = 50

combat_hit = ['magen', 'armen', 'huvudet', 'benet', 'skrevet']

player_one_trött = True
player_two_trött = True
player_one_sista = True
player_two_sista = True
player_turn = True

vapen = ['spikklubba', 'spjut', 'långsvärd', 'kortsvärd', 'dolk', 'inget vapen/händer']
skydd = ['ringbrynja', 'plåtrustning', 'läder', 'nakenhet']
sekundär = ['sköld', 'parrydolk', 'mini-armborst']

player_one_attack = 0
player_one_defence = 0
player_one_movement = 0
player_one_dmg = 0

player_two_attack = 0
player_two_defence = 0
player_two_movement = 0
player_two_dmg = 0

#-------------------------------------------Weapons and prep----------------------------------------



print ("Välkommen till mitt Den Stora Duellen!")
spelare_ett_namn = input("Skriv in namnet för krigare ett:")
spelare_två_namn = input("Skriv in namnet för krigare två:")
print (f"{spelare_ett_namn} och {spelare_två_namn} möter varandra i den stora arenan. Den med som först slår ned sin motståndare vinner! Må den bästa krigaren vinna!")
input("Tryck ENTER för att fortsätta.")

#forloop - komihåg att göra
print("En av fällgallrerna i arenan öppnas, ut går den lokala smeden Greger. Han bär en skåttskärra med vapen och utrustning.")
print("'Krigare, välj er utrustning!' ropar Greger.")
p1_vapen = input(f"{spelare_ett_namn}, välj ditt vapen! {vapen}")
p1_skydd = input(f"{spelare_ett_namn}, välj ditt skydd! {skydd}")
p1_sekundär = input(f"{spelare_ett_namn}, välj ditt sekundära vapen! {sekundär}")
p2_vapen = input(f"{spelare_två_namn}, välj ditt vapen! {vapen}")
p2_skydd = input(f"{spelare_två_namn}, välj ditt skydd! {skydd}")
p2_sekundär = input(f"{spelare_två_namn}, välj ditt sekundära vapen! {sekundär}")

spel_aktivitet = input("Starta Duellen?(Y/N)")
if spel_aktivitet == "N":
    print("Men varför är du ens här då? Fegis..")
#----------------------------------------------Vapenvärden---------------------------------
while True: 
    if spel_aktivitet == "N":
        break
#------Spelare Ett Vapenvärden
    if p1_vapen == "spikklubba":
        player_one_attack = random.randint(4,8)
        player_one_defence = random.randint(3,4)
        player_one_movement = random.randint(3,10)
        player_one_dmg = random.randint(3,9)
    elif p1_vapen == "spjut":
        player_one_attack = random.randint(6,9)
        player_one_defence = random.randint(2,7)
        player_one_movement = random.randint(5,9)
        player_one_dmg = random.randint(1,15)
    elif p1_vapen == "långsvärd":
        player_one_attack = random.randint(6,15)
        player_one_defence = random.randint(6,15)
        player_one_movement = random.randint(4,7)
        player_one_dmg = random.randint(10,20)
    elif p1_vapen == "kortsvärd":
        player_one_attack = random.randint(1,10)
        player_one_defence = random.randint(1,10)
        player_one_movement = random.randint(1,10)
        player_one_dmg = random.randint(1,10)
    elif p1_vapen == "dolk":
        player_one_attack = random.randint(5,6)
        player_one_defence = random.randint(1,2)
        player_one_movement = random.randint(7,13)
        player_one_dmg = random.randint,(5,6)
    elif p1_vapen == "inget vapen/händer":
        player_one_attack = random.randint(1,2)
        player_one_defence = random.randint(1,2)
        player_one_movement = 15
        player_one_dmg = random.randint(1,2)

    if p1_skydd == "ringbrynja":
        player_one_defence += 5
        player_one_movement -= 3 
        player_one_dmg -= 2
    elif p1_skydd == "plåtrustning":
        player_one_attack -= 4
        player_one_defence += 10
        player_one_movement -= 10 
        player_one_dmg -= 3
    elif p1_skydd == "läder":
        player_one_attack += 1
        player_one_defence += 2 
        player_one_dmg -= 1
    elif p1_skydd == "nakenhet":
        player_one_attack += 2
        player_one_defence -= 2
        player_one_movement += 2 
        player_one_dmg -= 2 

    if p1_sekundär == "sköld":
        player_one_attack += 1
        player_one_defence += 4
        player_one_movement -= 1 
        player_one_dmg += 1
    elif p1_sekundär == "parrydolk":
        player_one_attack -= 1
        player_one_defence += 2
        player_one_movement += 1 
        player_one_dmg -= 1
    elif p1_sekundär == "mini-armborst":
        player_one_attack += 5
        player_one_defence -= 1 
        player_one_dmg += 2

#-------Spelare Två Vapenvärden
    if p2_vapen == "spikklubba":
        player_two_attack = random.randint(4,8)
        player_two_defence = random.randint(3,4)
        player_two_movement = random.randint(3,10)
        player_two_dmg = random.randint(3,9)
    elif p2_vapen == "spjut":
        player_two_attack = random.randint(6,9)
        player_two_defence = random.randint(2,7)
        player_two_movement = random.randint(5,9)
        player_one_dmg = random.randint(1,15)
    elif p2_vapen == "långsvärd":
        player_two_attack = random.randint(6,15)
        player_two_defence = random.randint(6,15)
        player_two_movement = random.randint(4,7)
        player_two_dmg = random.randint(10,20)
    elif p2_vapen == "kortsvärd":
        player_two_attack = random.randint(1,10)
        player_two_defence = random.randint(1,10)
        player_two_movement = random.randint(1,10)
        player_two_dmg = random.randint(1,10)
    elif p2_vapen == "dolk":
        player_two_attack = random.randint(5,6)
        player_two_defence = random.randint(1,2)
        player_two_movement = random.randint(7,13)
        player_two_dmg = random.randint,(5,6)
    elif p2_vapen == "inget vapen/händer":
        player_two_attack = random.randint(1,2)
        player_two_defence = random.randint(1,2)
        player_two_movement = random.randint(10,15)
        player_two_dmg = random.randint(1,2)

    if p2_skydd == "ringbrynja":
        player_two_defence += 5
        player_two_movement -= 3 
        player_two_dmg -= 2
    elif p2_skydd == "plåtrustning":
        player_two_attack -= 4
        player_two_defence += 10
        player_two_movement -= 10 
        player_two_dmg -= 3
    elif p2_skydd == "läder":
        player_two_attack += 1
        player_two_defence += 2 
        player_two_dmg -= 1
    elif p2_skydd == "nakenhet":
        player_two_attack += 2
        player_two_defence -= 2
        player_two_movement += 2 
        player_two_dmg -= 2 

    if p2_sekundär == "sköld":
        player_two_attack += 1
        player_two_defence += 4
        player_two_movement -= 1 
        player_two_dmg += 1
    elif p2_sekundär == "parrydolk":
        player_two_attack -= 1
        player_two_defence += 2
        player_two_movement += 1 
        player_two_dmg -= 1
    elif p2_sekundär == "mini-armborst":
        player_two_attack += 5
        player_two_defence -= 1 
        player_two_dmg += 2







#------------------------------------------Combat-Loop-------------------------------------------------
    if player_turn is True: 
        if player_two_movement <= player_one_movement:
            if player_one_attack >= player_two_defence:
                print(f"{spelare_ett_namn} lyckas skada {spelare_två_namn} i {random.choice(combat_hit)} med sitt {p1_vapen}!")
                print(f"{spelare_ett_namn} för {player_one_dmg} skada på {spelare_två_namn}!")
                spelare_två_liv -= player_one_dmg
            elif player_two_defence > player_one_attack:
                print(f"{spelare_ett_namn} lyckas slå till {spelare_två_namn}, men {spelare_två_namn} lyckas skydda sig med sin {p2_skydd}!")
                print(f"Därför gör {spelare_ett_namn} ingen skada!")
        elif player_two_movement > player_one_movement:
            print(f"{spelare_två_namn} lyckas unvika {spelare_ett_namn}s attack mot {random.choice(combat_hit)}!")
            print(f"Därför lyckas {spelare_två_namn} inte göra någon skada!")
        player_turn = False
        input("Tryck ENTER för att fortsätta!")

    if player_turn is False:
        if player_two_movement >= player_one_movement:
            if player_two_attack >= player_one_defence:
                print(f"{spelare_två_namn} lyckas skada {spelare_ett_namn} i {random.choice(combat_hit)} med sitt {p2_vapen}!")
                print(f"{spelare_två_namn} för {player_two_dmg} skada på {spelare_ett_namn}!")
                spelare_ett_liv -= player_two_dmg
            elif player_one_defence > player_two_attack:
                print(f"{spelare_två_namn} lyckas slå till {spelare_ett_namn}, men {spelare_ett_namn} lyckas skydda sig med sin {p1_skydd}!")
                print(f"Därför gör {spelare_två_namn} ingen skada!")
        elif player_one_movement > player_two_movement:
            print(f"{spelare_ett_namn} lyckas undvika {spelare_två_namn}s attack mot {random.choice(combat_hit)}!")
            print(f"Därför lyckas {spelare_två_namn} inte göra någon skada!")
        player_turn = True
        input("Tryck ENTER för att fortsätta!")
    

    if spelare_ett_liv <= 25 and player_one_trött is True:
        print(f"{spelare_ett_namn} börjar att bli trött!")
        player_one_trött = False
        input("Tryck ENTER för att fortsätta.")
    elif spelare_två_liv <= 25 and player_two_trött is True:
        print(f"{spelare_två_namn} börjar att bli trött!")
        player_two_trött = False
        input("Tryck ENTER för att fortsätta.")
    elif spelare_ett_liv <= 5 and player_one_sista is True:
        print(f"{spelare_ett_namn} står på sina sista ben!")
        player_one_sista = False
        input("Tryck ENTER för att fortsätta.")
    elif spelare_två_liv <= 5 and player_two_sista is True:
        print(f"{spelare_två_namn} står på sina sista ben!")
        Player_two_sista = False
        input("Tryck ENTER för att fortsätta.")

    if spelare_ett_liv <= 0 or spelare_två_liv <= 0:
        if spelare_ett_liv <= 0:
            print(f"{spelare_två_namn} lyckas slå {spelare_ett_namn} till döds! {spelare_två_namn} vinner duellen!")
            break
        elif spelare_två_liv <= 0:
            print(f"{spelare_ett_namn} lyckas slå {spelare_två_namn} till döds! {spelare_ett_namn} vinner duellen!")
            break

   

#--------------------------------------------------------------------------------------
       