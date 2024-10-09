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
player_one_dmg = 0

player_two_attack = 0
player_two_defence = 0
player_two_movement = 0
player_two_dmg = 0

#-------------------------------------------Weapons and prep----------------------------------------



print ("Välkommen till mitt Den Stora Duellen! ")
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
if
#----------------------------------------------Vapenvärden---------------------------------

#------Spelare Ett Vapenvärden
if p1_vapen = "spikklubba":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_vapen = "spjut":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_vapen = "långsvärd":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_vapen = "kortsvärd":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_vapen = "dolk":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_vapen = "inget vapen/händer":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0

if p1_skydd = "ringbrynja":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_skydd = "plåtrustning":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_skydd = "läder":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_skydd = "naken":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0

if p1_sekundär = "sköld":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_sekundär = "parrydolk":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p1_sekundär = "mini-armborst":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0

#-------Spelare Två Vapenvärden
if p2_vapen = "spikklubba":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_vapen = "spjut":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_vapen = "långsvärd":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_vapen = "kortsvärd":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_vapen = "dolk":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_vapen = "inget vapen/händer":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0

if p2_skydd = "ringbrynja":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_skydd = "plåtrustning":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_skydd = "läder":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_skydd = "naken":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0

if p2_sekundär = "sköld":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_sekundär = "parrydolk":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0
elif: p2_sekundär = "mini-armborst":
    player_one_attack = 0
    player_one_defence = 0
    player_one_movement = 0 
    player_one_dmg = 0







#------------------------------------------Combat-Loop-------------------------------------------------

while True: 
    if spel_aktivitet == "N":
        break

    spelare_ett_combatroll = random.randint(1,20)
    spelare_två_combatroll = random.randint(1,20)
    
    if spelare_ett_combatroll > spelare_två_combatroll:
        spelare_två_liv -= 1
        print(f"{spelare_ett_namn} lyckas slå till {spelare_två_namn} i {random.choice(combat_hit)}!")
    elif spelare_två_combatroll > spelare_ett_combatroll:
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

    if spelare_ett_liv <= 0 or spelare_två_liv <= 0:
        if spelare_ett_liv <= 0:
            print(f"{spelare_två_namn} lyckas slå {spelare_ett_namn} till döds! {spelare_två_namn} vinner duellen!")
            break
        if spelare_två_liv <= 0:
            print(f"{spelare_ett_namn} lyckas slå {spelare_två_namn} till döds! {spelare_ett_namn} vinner duellen!")
            break

    input("Tryck ENTER för att fortsätta.")

#--------------------------------------------------------------------------------------
       