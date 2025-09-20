import random
from items import Items , Dic_items


#Classe qui s'occupe de la gestion du combat #

class lancement():
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1[0]
        self.pokemon2 = pokemon2[0]
        self.inventaire1 = [] 
        self.inventaire2 = [] 
        self.equipe1 = pokemon1
        self.equipe2 = pokemon2

   #Méthode qui permet de lancer le combat #

    def lancement_combat(self):
        rounds = 1
        print("combat lancé")
        mode = self.choix_mode_jeu() #0 correspond à du joueur contre joueur et 1 du joueur contre bot#
        items = self.choix_items()
        if mode == 0:
           for i in range(len(self.equipe1)):
            self.equipe1[i].remise_niveau()
           for i in range(len(self.equipe2)):
            self.equipe2[i].remise_niveau()
           if items == True: 
            self.initialiser_inventaires()
           while self.pokemon1.PV > 0 or self.pokemon2.PV > 0:
             if rounds == 1:
              print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
             print(f"Dresseur de {self.pokemon1.nom} que voulez vous faire ?")
             while True:
              res_pokemon1 = self.pokemon1.afficher_menu(self.pokemon1, 1)
              if res_pokemon1 == "changer":
                self.changer_pokemon(1)
                continue
              if res_pokemon1 == "items":
                self.utulisation_item(1)
                continue
              break  # ici res_pokemon1 est forcément une attaque valide (int)
             print(f"Dresseur de {self.pokemon2.nom} que voulez vous faire ?")
             while True:
              res_pokemon2 = self.pokemon2.afficher_menu(self.pokemon2, 1)
              if res_pokemon2 == "changer":
                self.changer_pokemon(1)
                continue
              if res_pokemon2 == "items":
                self.utulisation_item(1)
                continue
              break  # ici res_pokemon1 est forcément une attaque valide (int)
             premier = self.joue_en_premier(res_pokemon1,res_pokemon2)
             second = self.joue_en_second(premier)
             self.applications_statut(premier,second,rounds)
             print(f">>>>>>>>>> {premier.nom} commence <<<<<<<<<<<")
             if self.pokemon1 == premier:
              premier.degats(second,res_pokemon1,rounds)
             else:
              premier.degats(second,res_pokemon2,rounds)
             if second.PV <= 0:  
                print(f"{second.nom} a été vaincu!")
                break
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
             if self.pokemon1 == second:
               second.degats(premier,res_pokemon1,rounds) 
             else:
                second.degats(premier,res_pokemon2,rounds)
             if premier.PV <= 0:  
                print(f"{premier.nom} a été vaincu!")
                break
             rounds += 1
             print(f" >>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
        if mode == 1:
           joueur = self.choix_pokemon_bot()
           if joueur == self.pokemon1:
              bot = self.pokemon2
           else:
              bot = self.pokemon1
           
           # Remise à niveau pour toutes les équipes
           for i in range(len(self.equipe1)):
               self.equipe1[i].remise_niveau()
           for i in range(len(self.equipe2)):
               self.equipe2[i].remise_niveau()
           
           if items == True: 
               self.initialiser_inventaires()  # Utiliser la méthode correcte
           
           while joueur.PV > 0 and bot.PV > 0:  # Correction de la condition
             if rounds == 1:
                 print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
             
             print(f"Dresseur de {joueur.nom} que voulez vous faire ?")
             while True:
                 res_joueur = joueur.afficher_menu(joueur, 1)  # Ajout du paramètre equipe
                 if res_joueur == "changer":
                     # Déterminer quelle équipe correspond au joueur
                     equipe_joueur = 1 if joueur in self.equipe1 else 2
                     self.changer_pokemon(equipe_joueur)
                     # Mettre à jour la référence joueur après changement
                     joueur = self.pokemon1 if equipe_joueur == 1 else self.pokemon2
                     continue
                 if res_joueur == "items":
                     equipe_joueur = 1 if joueur in self.equipe1 else 2
                     self.utulisation_item(equipe_joueur)
                     continue
                 break  # res_joueur est une attaque valide
             
             # Le bot choisit une attaque aléatoirement
             res_bot = random.randint(1, len(bot.liste_attaques))
             
             premier = self.joue_en_premier(res_joueur, res_bot)
             second = self.joue_en_second(premier)
             self.applications_statut(premier, second, rounds)
             
             print(f">>>>>>>>>> {premier.nom} commence <<<<<<<<<<<")
             if premier == joueur:
                 premier.degats(second, res_joueur, rounds)
             else:
                 premier.degats(second, res_bot, rounds)
             
             if second.PV <= 0:  
                 print(f"{second.nom} a été vaincu!")
                 break
             
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<<")
             if second == joueur:
                 second.degats(premier, res_joueur, rounds) 
             else:
                 second.degats(premier, res_bot, rounds)
             
             if premier.PV <= 0:  
                 print(f"{premier.nom} a été vaincu!")
                 break
             
             rounds += 1
             print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
                 
   #Méthode qui demande le choix du mode de jeu : contre un joueur ou un bot#

    def choix_mode_jeu(self):
      while True:
        res = input("Voulez-vous jouer contre un joueur ou un bot ? (joueur/bot)\n> ") # \n permet de sauter la ligne pour la réponse  #
        if res == "joueur":
           return 0
        if res == "bot":
           return 1
        else:
          continue
          
  
   #Méthode#
    
    def choix_items(self):
      while True:
       res = input("Voulez-vous jouer avec des items ? (Oui/Non)\n> ")
       if res == "Oui":
          return True
       if res == "Non":
          return False
       else:
         continue


   #Méthode qui demande au joueur quel pokemon il veut jouer s'il souhaite jouer contre un bot#           

    def choix_pokemon_bot(self):
        res = input(f"lequel des 2 pokemons voulez vous etre le dresseur ?: ({self.pokemon1.nom}/{self.pokemon2.nom})\n> ")
        if res == self.pokemon1.nom:
           print(f"vous êtes désormais le dresseur de : {self.pokemon1.nom}" )
           return self.pokemon1
        if res == self.pokemon2.nom:
           print(f"vous êtes désormais le dresseur de : {self.pokemon2.nom}" )
           return self.pokemon2
        
   #Méthode qui définit qui joue en premier grâce à la vitesse des pokemons#

    def joue_en_premier(self,res_pokemon1,res_pokemon2):
       if self.pokemon1.liste_attaques[res_pokemon1 - 1].priorite > self.pokemon2.liste_attaques[res_pokemon2 - 1].priorite:
          return self.pokemon1
       if self.pokemon2.liste_attaques[res_pokemon2 - 1].priorite > self.pokemon1.liste_attaques[res_pokemon1 - 1].priorite:
          return self.pokemon2
       if self.pokemon1.vitesse > self.pokemon2.vitesse:
          return self.pokemon1
       if self.pokemon1.vitesse < self.pokemon2.vitesse:
          return self.pokemon2
       else:
         return random.choice([self.pokemon1, self.pokemon2]) #Si les deux ont la même vitesse#
       
   #Méthode qui définit qui joue en second par la vitesse#
       
    def joue_en_second(self,premier):
       if premier == self.pokemon1:
          return self.pokemon2
       if premier == self.pokemon2:
          return self.pokemon1
       
   #Méthode qui applique les effets des status#

    def applications_statut(self,premier,second,rounds):
       tuple = (premier,second)
       for i in range(len(tuple)):
        for j in range(len(tuple[i].effet)):
         if tuple[i].effet[j] == "burn":
          tuple[i].PV -= (tuple[i].PV // 8)
          print(f"{tuple[i].nom} subit les effets de ses brulures et perd {tuple[i].PV // 8} PV, il est désormais à {tuple[i].PV}")
         if tuple[i].effet[j] == "poison":
          tuple[i].PV -= (tuple[i].PV // 8)
          print(f"{tuple[i].nom} subit les effets de l'empoisonnement et perd {tuple[i].PV // 8} PV, il est désormais à {tuple[i].PV}")
         if tuple[i].effet[j] == "confusion":
          if tuple[i].effet_round_confusion == None:
             tuple[i].effet_round_confusion = rounds
             tuple[i].durée_confusion = random.randint(1,4)
          if rounds - tuple[i].effet_round_confusion < tuple[i].durée_confusion:
             if random.randint(1,2) == 1:
                degats_confusion = int((((((tuple[i].niveau * 0.4 + 2) * 40) * tuple[i].attaque /  tuple[i].defense ) / 50 ) + 2) * random.uniform(0.85,1))
                tuple[i].PV -= degats_confusion
                print(f"{tuple[i].nom} subit les effets de la confusion et perd {degats_confusion} PV, il a désormais {tuple[i].PV} PV")
             else:
                print(f"{tuple[i].nom} surmonte sa confusion ce tour-ci")
          else:
             print(f"{tuple[i].nom} n'est plus confus.")
             tuple[i].effet.remove("confusion")
             tuple[i].effet_round_confusion = None
             tuple[i].confusion_duree = None
             tuple[i].nom = tuple[i].nom.replace("(confus)", "")

                   #Les effets de la paralysie et du sommeil sont pris en compte dans miss()
                   
    def changer_pokemon(self, equipe):
     if equipe == 1:
        print("Pokémons disponibles équipe 1 :")
        for i, p in enumerate(self.equipe1, 1):
            etat = "KO" if p.PV <= 0 else f"{p.PV} PV"
            actif = "(actif)" if p == self.pokemon1 else ""
            print(f"{i}. {p.nom} - {etat} {actif}")
        choix = int(input("Choix : "))
        if 1 <= choix <= len(self.equipe1):
            nouveau = self.equipe1[choix - 1]
            if nouveau.PV > 0 and nouveau != self.pokemon1:
                self.pokemon1 = nouveau
                print(f"Vous envoyez {nouveau.nom} au combat !")
            else:
                print("Choix invalide (KO ou déjà actif)")
     elif equipe == 2:
        print("Pokémons disponibles équipe 2 :")
        for i, p in enumerate(self.equipe2, 1):
            etat = "KO" if p.PV <= 0 else f"{p.PV} PV"
            actif = "(actif)" if p == self.pokemon2 else ""
            print(f"{i}. {p.nom} - {etat} {actif}")
        choix = int(input("Choix : "))
        if 1 <= choix <= len(self.equipe2):
            nouveau = self.equipe2[choix - 1]
            if nouveau.PV > 0 and nouveau != self.pokemon2:
                self.pokemon2 = nouveau
                print(f"Vous envoyez {nouveau.nom} au combat !")
            else:
                print("Choix invalide (KO ou déjà actif)")

    def initialiser_inventaires(self):
     self.inventaire1 = []
     self.inventaire2 = []

     for nom, item in Dic_items.items():
        quantite = input(f"Quelle quantité voulez-vous attribuer à l'objet : {item.nom} ? (Pour les 2 équipes)\n> ")

        while not quantite.isdigit():
            print("Entrée invalide. Veuillez entrer un nombre entier positif ou nul.")
            quantite = input(f"Quelle quantité voulez-vous attribuer à l'objet : {item.nom} ? (Pour les 2 équipes)\n> ")

        quantite = int(quantite)

        item1 = item.copier_items()
        item1.quantite = quantite
        self.inventaire1.append(item1)

        item2 = item.copier_items()
        item2.quantite = quantite
        self.inventaire2.append(item2)
      
    def utulisation_item(self,equipe):
       inventaire = self.inventaire1 if equipe == 1 else self.inventaire2
       if inventaire == self.inventaire1:
         pokemon = self.pokemon1
       else:
         pokemon = self.pokemon2

       for i, items in enumerate(inventaire, 1):
            print(f"{i}. {items.nom}: PV: {items.PV_item},PP: {items.PP_item}, quantité: {items.quantite},description: {items.description}")
       res = input()
       if res.isdigit() and 0 < int(res) <= len(inventaire):
        choix = int(res) - 1
        item = inventaire[choix] 
        if item.nom == "Potion" and item.quantite > 0:
          if item.PV_item + pokemon.PV  > pokemon.stats_originales[1]:
             pokemon.PV = pokemon.stats_originales[1]
          else:
           pokemon.PV += 20
          item.quantite -= 1
          print(f"L'utulisation d'une potion permet à {pokemon.nom} de regagner 20 PV , {pokemon.nom} est désormais à {pokemon.PV} PV")

        if item.nom == "Hyper-potion" and item.quantite > 0:
          if item.PV_item + pokemon.PV  > pokemon.stats_originales[1]:
             pokemon.PV = pokemon.stats_originales[1]
          else:
           pokemon.PV += 200
          item.quantite -= 1
          print(f"L'utulisation d'une Hyper-potion permet à {pokemon.nom} de regagner 200 PV , {pokemon.nom} est désormais à {pokemon.PV} PV")

        if item.nom == "Super-potion" and item.quantite > 0:
          if item.PV_item + pokemon.PV  > pokemon.stats_originales[1]:
             pokemon.PV = pokemon.stats_originales[1]
          else:
           pokemon.PV += 50
          item.quantite -= 1
          print(f"L'utulisation d'une Super-potion permet à {pokemon.nom} de regagner 50 PV , {pokemon.nom} est désormais à {pokemon.PV} PV")

        if item.nom == "Guerison" and item.quantite > 0:
          pokemon.PV = pokemon.stats_originales[1]
          item.quantite -= 1
          for effet in pokemon.effet[:]:  # copie de la liste
           if effet == "burn":
            pokemon.attaque *= 2
           elif effet == "paralysie":
            pokemon.vitesse *= 4
            pokemon.effet.remove(effet)
          pokemon.nom = pokemon.stats_originales[0]
          print(f"L'utulisation d'un objet de guérison permet à {pokemon.nom} de regagner l'entiereté de ses PV et de supprimer ses effets de statut")

        if item.nom == "Potion-max" and item.quantite > 0:
          pokemon.PV = pokemon.stats_originales[1]
          item.quantite -= 1
          print(f"L'utulisation d'une potion max permet à {pokemon.nom} de regagner l'entiereté de ses PV")

        if item.nom == "Total-soin" and item.quantite > 0:
          item.quantite -= 1
          for effet in pokemon.effet[:]:  # copie de la liste
           if effet == "burn":
            pokemon.attaque *= 2
           elif effet == "paralysie":
            pokemon.vitesse *= 4
            pokemon.effet.remove(effet)
          pokemon.nom = pokemon.stats_originales[0]
          print(f"L'utulisation d'un total-soin permet à {pokemon.nom} de guérir de tous ses effets de statut")

        if item.nom == "Antidote" and item.quantite > 0 and "poison" in pokemon.effet:
          pokemon.effet.remove("poison")
          pokemon.nom = pokemon.nom.replace("(empoisonné)", "")
          item.quantite -= 1
          print(f"L'utulisation d'un Antidote permet à {pokemon.nom} de guérir de som empoisonnement")

        if item.nom == "Anti-brulure" and item.quantite > 0 and "burn" in pokemon.effet:
          pokemon.effet.remove("burn")
          pokemon.nom = pokemon.nom.replace("(brulé)", "")
          item.quantite -= 1
          pokemon.attaque = pokemon.attaque * 2
          print(f"L'utulisation d'un Anti-brulure permet à {pokemon.nom} de guérir de sa brulure")

        if item.nom == "Reveil" and item.quantite > 0 and "sommeil" in pokemon.effet:
          pokemon.effet.remove("sommeil")
          pokemon.nom = pokemon.nom.replace("(ZzzzZ)", "")
          item.quantite -= 1
          print(f"L'utulisation d'un réveil permet à {pokemon.nom} de se reveiller")

        if item.nom == "Anti-Para" and item.quantite > 0 and "paralysie" in pokemon.effet:
          pokemon.effet.remove("paralysie")
          pokemon.nom = pokemon.nom.replace("(paralysé)", "")
          item.quantite -= 1
          pokemon.vitesse = pokemon.vitesse * 4
          print(f"L'utulisation d'un Anti-Para permet à {pokemon.nom} de guérir sa paralysie")

      

    


