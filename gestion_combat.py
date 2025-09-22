import random
from items import Items , Dic_items , Dic_items_tenus

class lancement():
  "Initialisation de la classe lancement , en entrée on prend les 2 équipes de pokémons , elle ne renvoie rien , mais initialise les inventaires des 2 équipes"
  "dit quel est le pokémon choisi dans les équipes pokemon1 ou 2 [0]"
  def __init__(self,pokemon1:list,pokemon2:list) -> None:
    self.pokemon1 = pokemon1[0]
    self.pokemon2 = pokemon2[0]
    self.inventaire1: list[Items] = [] 
    self.inventaire2: list[Items] = [] 
    self.equipe1: list = pokemon1 # type: list[Pokemon]
    self.equipe2: list = pokemon2 # type: list[Pokemon]

  def lancement_combat(self) -> None:
    "Classe Majeur du code qui s'occupe de gérer le déroulement du combat, elle ne prend aucun argument en entrée et n'en ressort aucun"
    rounds : int = 1
    print("combat lancé")
    mode : int = self.choix_mode_jeu() #0 correspond à du joueur contre joueur et 1 du joueur contre bot#
    items : bool = self.choix_items()
    self.objets_tenus()
    self.utulisation_objets_tenus()
    if mode == 0:
      for i in range(len(self.equipe1)):
        self.equipe1[i].remise_niveau()
      for i in range(len(self.equipe2)):
        self.equipe2[i].remise_niveau()
      if items == True: 
        self.initialiser_inventaires()
      while any(p.PV > 0 for p in self.equipe1) or any(p.PV > 0 for p in self.equipe2):
        if rounds == 1:
          print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
        retour_gagnant = self.verif_gagnant()
        if retour_gagnant == 1 or retour_gagnant == 2:
          break
        self.verif_mort(self.pokemon1,self.pokemon2)
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
          res_pokemon2 = self.pokemon2.afficher_menu(self.pokemon2, 2)
          if res_pokemon2 == "changer":
            self.changer_pokemon(2)
            continue
          if res_pokemon2 == "items":
            self.utulisation_item(2)
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
        print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
        if self.pokemon1 == second:
          second.degats(premier,res_pokemon1,rounds) 
        else:
          second.degats(premier,res_pokemon2,rounds)
        rounds += 1
        print(f" >>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
    if mode == 1:
      joueur = self.choix_pokemon_bot()
      if joueur == self.pokemon1:
        bot = self.pokemon2
        bot.mode = 1
      else:
        bot = self.pokemon1
        bot.mode = 1
      for i in range(len(self.equipe1)):
        self.equipe1[i].remise_niveau()
      for i in range(len(self.equipe2)):
        self.equipe2[i].remise_niveau()
      if items == True: 
        self.initialiser_inventaires()  
      while any(p.PV > 0 for p in self.equipe1) or any(p.PV > 0 for p in self.equipe2): 
        if rounds == 1:
          print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
        retour_gagnant = self.verif_gagnant()
        if retour_gagnant == 1 or retour_gagnant == 2:
          break
        self.verif_mort(joueur,bot)
        if joueur.PV <= 0:
          joueur = self.pokemon1 if joueur in self.equipe1 else self.pokemon2
        if bot.PV <= 0:
          bot = self.pokemon1 if bot in self.equipe1 else self.pokemon2
        print(f"Dresseur de {joueur.nom} que voulez vous faire ?")
        while True:
          res_joueur = joueur.afficher_menu(joueur, 1)  
          if res_joueur == "changer":
            equipe_joueur = 1 if joueur in self.equipe1 else 2
            self.changer_pokemon(equipe_joueur)
            joueur = self.pokemon1 if equipe_joueur == 1 else self.pokemon2
            continue
          if res_joueur == "items":
            equipe_joueur = 1 if joueur in self.equipe1 else 2
            self.utulisation_item(equipe_joueur)
            continue
          break  
        res_bot = random.randint(1, len(bot.liste_attaques))
        premier = self.joue_en_premier(res_joueur, res_bot)
        second = self.joue_en_second(premier)
        self.applications_statut(premier, second, rounds)
        print(f">>>>>>>>>> {premier.nom} commence <<<<<<<<<<<")
        if premier == joueur:
          premier.degats(second, res_joueur, rounds)
        else:
          premier.degats(second, res_bot, rounds)
        print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<<")
        if second == joueur:
          second.degats(premier, res_joueur, rounds) 
        else:
          second.degats(premier, res_bot, rounds)
        rounds += 1
        print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
                 
  def choix_mode_jeu(self) -> int:
    "Méthode qui demande à l'utulisateur s'il veut faire du joueur contre joueur ou du joueur contre bot , elle ne prend rien en entrée et renvoie 0(en cas de joueur contre joueur)"
    "et 1(en cas de joueur contre bot) , utulisée dans lancement_combat()"
    while True:
      res = input("Voulez-vous jouer contre un joueur ou un bot ? (joueur/bot)\n> ") # \n permet de sauter la ligne pour la réponse  #
      if res == "joueur":
        return 0
      if res == "bot":
        return 1
      else:
        continue
    
  def choix_items(self) -> bool:
    "Méthode qui demande à l'utulisateur s'il veut jouer avec des items , elle ne prend aucune entrée et renvoie True si Oui et False si Non , utulisée dans  lancement_combat() "
    while True:
      res = input("Voulez-vous jouer avec des items ? (Oui/Non)\n> ")
      if res == "Oui":
        return True
      if res == "Non":
        return False
      else:
        continue        

  def choix_pokemon_bot(self):
    "Méthode qui est utulisé si l'utulisateur choisi de faire du joueur contre bot,elle demande à l'utulisateur dans quelle équipe il veut jouer , elle ne prend rien en entrée et renvoie self.pokemon1 si le joueur"
    "veut jouer dans l'équipe 1 et self.pokemon2 s'il veut jouer avec l'équipe 2, utulisée dans lancement_combat()"
    res = input(f"lequel des 2 pokemons voulez vous etre le dresseur ?: ({self.pokemon1.nom}/{self.pokemon2.nom})\n> ")
    if res == self.pokemon1.nom:
      print(f"vous êtes désormais le dresseur de : {self.pokemon1.nom}" )
      return self.pokemon1
    if res == self.pokemon2.nom:
      print(f"vous êtes désormais le dresseur de : {self.pokemon2.nom}" )
      return self.pokemon2
        
  def joue_en_premier(self,res_pokemon1 : int ,res_pokemon2 : int):
    "Méthode qui est utulisée pour savoir lequel des 2 pokémons va attaquer en premier , elle prend en entrée les numéros des attaques des 2 pokémons chacun(par exemple 3 de salameche c'est flammèche et on revient à ça dans la fonction),"
    "elle va renvoyer self.pokemon1 ou self.pokemon2 en fonction de qui va attaquer, utulisée dans lancement_combat()"
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
       
  def joue_en_second(self,premier):
    "Méthode en parallèle de joue_en_premier qui détermine qui joue en second ,elle prend en argument le premier(résultat de joue_en_premier , celui qui joue en premier) et renvoie le second , tout simplement "
    "celui qui a pas été selectionné par joue_en_premier, utulisée dans lancement_combat()"
    if premier == self.pokemon1:
      return self.pokemon2
    if premier == self.pokemon2:
      return self.pokemon1

  def applications_statut(self,premier,second,rounds : int)  -> None:
    "Méthode qui gère l'application des status qui font des dégats , elle prend en argument le premier , le second et les rounds, et ne renvoie rien , son utulité est d'infliger les dégats par les statuts comme les brulures ou le poison"
    "l'utulisation de premier et second ne révèle pas d'un ordre de passage de concret mais juste d'utulité et les rounds sont pris en compte pour confusion qui n'est pas un effet illimité , utulisée dans lancement_combat()"
    tuple = (premier,second)
    for i in range(len(tuple)):
      for j in range(len(tuple[i].effet)):
        if tuple[i].effet[j] == "burn":
          tuple[i].PV -= (tuple[i].stats_originales[1] // 8)
          print(f"{tuple[i].nom} subit les effets de ses brulures et perd {tuple[i].stats_originales[1] // 8} PV, il est désormais à {tuple[i].PV}")
        if tuple[i].effet[j] == "poison":
          tuple[i].PV -= (tuple[i].stats_originales[1] // 8)
          print(f"{tuple[i].nom} subit les effets de l'empoisonnement et perd {tuple[i].stats_originales[1] // 8} PV, il est désormais à {tuple[i].PV}")
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
                   
  def changer_pokemon(self, equipe: int)  -> None:
    "Méthode qui permet de changer de pokemon , elle prend en argument l'équipe qui doit changer de pokémon et ne renvoie rien , le bot prend le premier de la liste qui a plus de 0 PV ,le joueur peut faire son choix"
    ", utulisée dans lancement_combat()"
    if equipe == 1:
      if self.pokemon1.mode == 1: # si c'est un bot"
        for p in self.equipe1:
          if p.PV > 0 and p != self.pokemon1:
            self.pokemon1 = p
            print(f"Le bot envoie {p.nom} au combat !")
            return
      print("Pokémons disponibles équipe 1 :")
      for i, p in enumerate(self.equipe1, 1):
        etat = "KO" if p.PV <= 0 else f"{p.PV} PV"
        actif = "(actif)" if p == self.pokemon1 else ""
        print(f"{i}. {p.nom} - {etat} {actif}")

      while True:
        choix = input("Choix : ")
        if choix.isdigit():
          choix = int(choix)
          if 1 <= choix <= len(self.equipe1):
            nouveau = self.equipe1[choix - 1]
            if nouveau.PV > 0 and nouveau != self.pokemon1:
              self.pokemon1 = nouveau
              print(f"Vous envoyez {nouveau.nom} au combat !")
              break
            else:
              if nouveau.PV <= 0:
                print("Ce Pokémon est KO, choisissez-en un autre.")
                continue
              else:
                print("Ce Pokémon est déjà actif dans l'équipe.")
                continue
          else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            continue
        else:
          print("Veuillez entrer un nombre entier valide.")
          continue

    elif equipe == 2:
      if self.pokemon2.mode == 1: # si c'est un bot"
        for p in self.equipe2:
          if p.PV > 0 and p != self.pokemon2:
            self.pokemon2 = p
            print(f"Le bot envoie {p.nom} au combat !")
            return
      print("Pokémons disponibles équipe 2 :")
      for i, p in enumerate(self.equipe2, 1):
            etat = "KO" if p.PV <= 0 else f"{p.PV} PV"
            actif = "(actif)" if p == self.pokemon2 else ""
            print(f"{i}. {p.nom} - {etat} {actif}")
      while True:
        choix = input("Choix : ")
        if choix.isdigit():
          choix = int(choix)
          if 1 <= choix <= len(self.equipe2):
            nouveau = self.equipe2[choix - 1]
            if nouveau.PV > 0 and nouveau != self.pokemon2:
              self.pokemon2 = nouveau
              print(f"Vous envoyez {nouveau.nom} au combat !")
              break
            else:
              if nouveau.PV <= 0:
                print("Ce Pokémon est KO, choisissez-en un autre.")
                continue
              else:
                print("Ce Pokémon est déjà actif dans l'équipe.")
                continue
          else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            continue
        else:
          print("Veuillez entrer un nombre entier valide.")
          continue

  def initialiser_inventaires(self)  -> None:
    "Méthode qui initialise les inventaires des 2 équipes , elle ne prend rien en argument et ne renvoie rien, elle demande à l'utulisateur la quantité qu'il veut pour chacun des  objets des 2 équipes , utulisée dans lancement_combat()"
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

  def utiliser_rappel(self, equipe : list) -> object | None:
    "Méthode qui permet l'utulisation des rappels , elle prend en argument la liste qui correspond aux 2 équipes (equipe_rappel dans l'utulisation de rappel et rappel max dans utulisation_item) et ne renvoie rien"
    "Elle affiche donc la liste des pokémons KO de l'équipe et permet de les réanimer, utulisée dans lancement_combat() "
    ko_pokemons = [p for p in equipe if p.PV <= 0]
    if not ko_pokemons:
      print("Aucun Pokémon K.O. dans cette équipe.")
      return
    print("Pokémons K.O. disponibles :")
    for i, p in enumerate(ko_pokemons, 1):
      print(f"{i}. {p.nom}")
    choix = input("Choisissez un Pokémon à réanimer:\n> ")
    if not choix.isdigit() or not (1 <= int(choix) <= len(ko_pokemons)):
      print("Choix invalide.")
      return
    pokemon = ko_pokemons[int(choix) - 1]
    return pokemon
      
  def utulisation_item(self,equipe: int) -> None:
    "Méthode qui permet d'utuliser les items dans l'inventaire, elle prend en argument l'équipe(le chiffre de l'équipe 1 ou 2) et ne renvoie rien, utulisée dans lancement_combat()"
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

      if item.nom == "Anti-gel" and item.quantite > 0 and "gelé" in pokemon.effet:
        pokemon.effet.remove("gelé")
        pokemon.nom = pokemon.nom.replace("(gelé)", "")
        item.quantite -= 1
        print(f"L'utulisation d'un Anti-gel permet à {pokemon.nom} de guérir de son dégel")
          
      if item.nom == "Rappel max" and item.quantite > 0:
        equipe_rappel = self.equipe1 if equipe == 1 else self.equipe2
        pokemon = self.utiliser_rappel(equipe_rappel)
        if pokemon: # si la méthode utuliser_rappel n'a pas renvoyé de pokémon#
          pokemon.PV = pokemon.stats_originales[1]
          item.quantite -= 1
          print(f"L'utulisation d'un rappel max permet à {pokemon.nom} de regagner l'entiereté de ses PV et de revenir au combat")

      if item.nom == "Rappel" and item.quantite > 0:
        equipe_rappel = self.equipe1 if equipe == 1 else self.equipe2
        pokemon = self.utiliser_rappel(equipe_rappel)
        if pokemon: # si la méthode utuliser_rappel n'a pas renvoyé de pokémon#
          pokemon.PV = pokemon.stats_originales[1] // 2
          item.quantite -= 1
          print(f"L'utulisation d'un rappel permet à {pokemon.nom} de regagner la moitié de ses PV et de revenir au combat")
        
  def verif_mort(self,pokemon1,pokemon2) -> None:
    "Méthode qui vérifie si l'un des deux pokémon combattant est mort et oblige à changer de pokémon , elle prend en argument les deux pokémons combattants et ne renvoie rien, utulisée dans lancement_combat()"
    if pokemon1.PV <= 0:
      print(f"{pokemon1.nom} est KO , changement de pokémon")
      self.changer_pokemon(1)
    if pokemon2.PV <= 0:
      print(f"{pokemon2.nom} est KO , changement de pokémon")
      self.changer_pokemon(2)

  def verif_gagnant(self) -> int:
    "Méthode qui vérifie si l'une des 2 équipes a gagné , elle prend rien en argument et renvoie le numéro de l'équipe gagnante, utulisé dans lancement_combat()"
    equipe1_KO = all(p.PV <= 0 for p in self.equipe1)
    equipe2_KO = all(p.PV <= 0 for p in self.equipe2)

    if equipe1_KO:
      print("Tous les Pokémon de l'équipe 1 sont KO. Équipe 2 a gagné !")
      return 2
    elif equipe2_KO:
      print("Tous les Pokémon de l'équipe 2 sont KO. Équipe 1 a gagné !")
      return 1
    else:
      return 0  

  def objets_tenus(self) -> None:
    "Méthode qui demande à l'utulisateur s'il veut rajouter des items à tenir aux pokémons et qui permet de leur les attribuer , elle ne prend rien en argument et ne renvoie rien, utulisée dans lancement_combat()"
    while True:
      res = input("Voulez-vous rajouter des items à tenir ? (Oui/Non)\n> ")
      if res == "Oui": 

        while True:
          if not Dic_items_tenus:
            print("Tous les objets ont été attribués !")
            return
        
          # --- ÉQUIPE 1 --- #
          print("<<< Pour les pokémons de l'équipe 1 >>>")
          for i, p in enumerate(self.equipe1, 1):
            held = f"(tient: {p.held_item.nom})" if hasattr(p, "held_item") and p.held_item else "(aucun objet)"
            print(f"{i}. {p.nom} {held}")
          while True:
            res_pokemon = input("Choisissez un Pokémon (numéro) ou 'q' pour quitter :\n> ")
            if res_pokemon == "q":
              return
            if res_pokemon.isdigit() and 1 <= int(res_pokemon) <= len(self.equipe1):
              pokemon = self.equipe1[int(res_pokemon) - 1]
              if pokemon.held_item != None:
                continue
              break
            print("Choix de Pokémon invalide. Réessayez.")
          while True:
            print("<<< Objets disponibles >>>")
            for i, (nom, item) in enumerate(Dic_items_tenus.items(), 1):
              print(f"{i}. {nom} - {item.description}")
            res_item = input("Choisissez un objet (numéro) ou 'q' pour quitter :\n> ")
            if res_item == "q":
              return
            if res_item.isdigit() and 1 <= int(res_item) <= len(Dic_items_tenus):
              item_nom = list(Dic_items_tenus.keys())[int(res_item) - 1]
              item = Dic_items_tenus.pop(item_nom).copier_items()  #supprime et copie l'objet
              pokemon.held_item = item
              print(f"{pokemon.nom} tient maintenant {item.nom} !")
              break
            print("Choix d’objet invalide ou le pokémon a déja un item. Réessayez.")
          if not Dic_items_tenus:
            print("Tous les objets ont été attribués !")
            return

          # --- ÉQUIPE 2 --- #
          print("\n<<< Pour les pokémons de l'équipe 2 >>>")
          for i, p in enumerate(self.equipe2, 1):
            held = f"(tient: {p.held_item.nom})" if hasattr(p, "held_item") and p.held_item else "(aucun objet)"
            print(f"{i}. {p.nom} {held}")
          while True:
            res_pokemon = input("Choisissez un Pokémon (numéro) ou 'q' pour quitter :\n> ")
            if res_pokemon == "q":
              return
            if res_pokemon.isdigit() and 1 <= int(res_pokemon) <= len(self.equipe2):
              pokemon = self.equipe2[int(res_pokemon) - 1]
              if pokemon.held_item != None:
                continue
              break
            print("Choix de Pokémon invalide. Réessayez.")
          while True:
            print("<<< Objets disponibles >>>")
            for i, (nom, item) in enumerate(Dic_items_tenus.items(), 1):
              print(f"{i}. {nom} - {item.description}")
            res_item = input("Choisissez un objet (numéro) ou 'q' pour quitter :\n> ")
            if res_item == "q":
              return
            if res_item.isdigit() and 1 <= int(res_item) <= len(Dic_items_tenus):
              item_nom = list(Dic_items_tenus.keys())[int(res_item) - 1]
              item = Dic_items_tenus.pop(item_nom).copier_items()
              pokemon.held_item = item
              print(f"{pokemon.nom} tient maintenant {item.nom} !")
              break
            print("Choix d’objet invalide ou le pokémon à deja un item. Réessayez.")

      if res == "Non":
        return

  def utulisation_objets_tenus(self) -> None:
    "Méthode qui applique les effets des objets tenus , elle prend rien en argument et renvoie rien, utulisée dans lancement_combat()"
    equipes = (self.equipe1,self.equipe2)
    for equipe in equipes:
      for pokemon in equipe:
           
        if pokemon.held_item and pokemon.held_item.nom == "Protéine":
          pokemon.attaque += 10
          
        if pokemon.held_item and pokemon.held_item.nom == "Fer":
          pokemon.defense += 10
            
        if pokemon.held_item and pokemon.held_item.nom == "PV plus":
          pokemon.PV += 10


          
              


    


