import random
import time
 
CASE_OIE = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
CASE_PONT = 6
CASE_HOTEL = 19
CASE_PUITS = 31
CASE_PRISON = 52
CASE_LABYRINTHE = 42
CASE_RETOUR_DEBUT = 58

joueurs = []

def lancer_des():
    return random.randint(1, 6), random.randint(1, 6)

def avancer_pion(joueur, de1, de2, message_affiche = True):
    total = de1 + de2
    case_actuelle = joueur['position']
    nouvelle_case = case_actuelle + total

    if nouvelle_case > 63:
        joueur['position'] = 63 - (nouvelle_case - 63)
    else:
        joueur['position'] = nouvelle_case

    while joueur['position'] in CASE_OIE and joueur['position'] != CASE_PRISON and joueur['position'] != CASE_PUITS:
        avancer_pion(joueur, de1, de2, message_affiche = False)

    if joueur['position'] == CASE_PONT:
        print(f"Joueuse {joueur['numero']}: Vous passez sur le pont et atterrissez case 12")
        joueur['position'] = 12
        
    elif joueur['position'] == CASE_HOTEL:
        joueur['wait'] = 1
        print("Vous avez sommeil. Vous vous arrêtez à l'hôtel pour la nuit.")
        
    elif case_actuelle == 0:
        if (de1 == 4 and de2 == 5) or (de1 == 5 and de2 == 4):
            joueur['position'] = 53
            print(f"Joueuse {joueur['numero']}: Quelle chance, vous voici propoulsée à la case 53 !")
        elif (de1 == 6 and de2 == 3) or (de1 == 3 and de2 == 6):
            joueur['position'] = 26
            print(f"Joueuse {joueur['numero']}: Joli coup ! Vous voici maintenant à la case 26.")

    elif joueur['position'] == CASE_PUITS:
        if message_affiche:
            print(f"Joueuse {joueur['numero']}: Vous êtes tombée dans le puits !")
    elif joueur['position'] == CASE_PRISON:
        if message_affiche:
            print(f"Joueuse {joueur['numero']}: Vous êtes tombée en prison !")
    
    if joueur['position'] == CASE_LABYRINTHE:
            joueur['position'] = 30
            if message_affiche:
                print(f"Joueuse {joueur['numero']}: Labyrinthe ! Vous vous êtes perdue. Retour à la case 30...")


    elif joueur['position'] == CASE_RETOUR_DEBUT:
            joueur['position'] = 0
            print(f"Joueuse {joueur['numero']}: Case 58, retour au début...")

def partie():
    n = int(input("Combien de joueurs ?"))
    joueurs = [{'numero': i + 1, 'position': 0, 'wait' : 0, 'last_pos' : 0} for i in range(n)]
    ordre_joueurs = sorted(joueurs, key=lambda j: random.randint(1, 6) + random.randint(1, 6), reverse=True)    
    
    print("Ordre des joueurs :")
    for joueur in ordre_joueurs:
        print(f"Joueur {joueur['numero']}")
    
    tour = 0

    while True:
        tour += 1
            
        time.sleep(2)
        print(f"\nTour {tour}")
        
        for joueur in ordre_joueurs:
            if joueur['position'] != CASE_PUITS and joueur['position'] != CASE_PRISON:
                if joueur["wait"] == 0:
                    print(f"Joueuse {joueur['numero']}: case {joueur['position']}")
                    joueur['last_pos'] = joueur['position']
                    de1, de2 = lancer_des()
                    print(f"Lancers de dés : {de1}, {de2}")  
                    avancer_pion(joueur, de1, de2)
                else:
                    print(f"Joueuse {joueur['numero']}: Vous êtes à l'hôtel. Vous passez votre tour.")
                    joueur['wait'] = 0
            for autre_joueur in joueurs:
                if autre_joueur['position'] == joueur['position'] and autre_joueur is not joueur:
                    print(f"Échange de positions entre joueuse {joueur['numero']} et joueuse {autre_joueur['numero']} !")
                    autre_joueur['position'] = joueur['last_pos']
                    print(f"La joueuse {autre_joueur['numero']} est maintenant à la case {autre_joueur['position']}")
    
            print(f"Joueuse {joueur['numero']}: case {joueur['position']}")
    
            if joueur['position'] == 63:
                print(f"La joueuse {joueur['numero']} a gagné !")
                print("\nClassement final :")
                classement = sorted(joueurs, key=lambda j: j['position'], reverse=True)
                for i, joueur in enumerate(classement):
                    print(f"{i+1}. - Joueuse {joueur['numero']}, {joueur['position']}")
                return
    
        if all(joueur["position"] == CASE_PUITS or joueur['position'] == CASE_PRISON for joueur in ordre_joueurs):
            print("Toutes les joueuses sont coincées.")
            return
        
                    
partie()