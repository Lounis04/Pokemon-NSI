from attaques import Dic_attaques
from items import Dic_items
import random

#Dictionnaire des types dans pokemon génération 3#
type_dic = {
    "Normal": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 2, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 0.5,"Spectre": 0,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Feu": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 2, "Electrik": 1, "Glace": 2, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 2,"Roche": 0.5,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 2},
    "Eau": {"Normal": 1, "Feu": 2, "Eau": 0.5, "Plante": 0.5, "Electrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 2,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 2,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 1},
    "Plante": {"Normal": 1, "Feu": 0.5, "Eau": 2, "Plante": 0.5, "Electrik": 1, "Glace": 1, "Combat": 1, "Poison": 0.5 ,"Sol": 2,"Vol": 0.5,"Psy": 1,"Insecte": 0.5,"Roche": 2,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 0.5},
    "Electrik": {"Normal": 1, "Feu": 1, "Eau": 2, "Plante": 0.5, "Electrik": 0.5, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 0,"Vol": 2,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 1},
    "Glace": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 2, "Electrik": 1, "Glace": 0.5, "Combat": 1, "Poison": 1 ,"Sol": 2,"Vol": 2,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 2,"Tenebres": 1,"Acier": 0.5},
    "Combat": {"Normal": 2, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 2, "Combat": 1, "Poison": 0.5 ,"Sol": 1,"Vol": 0.5,"Psy": 0.5,"Insecte": 0.5,"Roche": 2,"Spectre": 0,"Dragon": 1,"Tenebres": 2,"Acier": 2},
    "Poison": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 2, "Electrik": 1, "Glace": 1, "Combat": 1, "Poison": 0.5 ,"Sol": 0.5,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 0.5,"Spectre": 0.5,"Dragon": 1,"Tenebres": 1,"Acier": 0},
    "Sol": {"Normal": 1, "Feu": 2, "Eau": 1, "Plante": 0.5, "Electrik": 2, "Glace": 1, "Combat": 1, "Poison": 2 ,"Sol": 1,"Vol": 0,"Psy": 1,"Insecte": 0.5,"Roche": 2,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 2},
    "Vol": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 2, "Electrik": 0.5, "Glace": 1, "Combat": 2, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 2,"Roche": 0.5,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Psy": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 2, "Poison": 2 ,"Sol": 1,"Vol": 1,"Psy": 0.5,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 1,"Tenebres": 0,"Acier": 0.5},
    "Insecte": {"Normal": 1, "Feu": 0.5, "Eau": 1, "Plante": 2, "Electrik": 1, "Glace": 1, "Combat": 0.5, "Poison": 0.5 ,"Sol": 1,"Vol": 0.5,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 0.5,"Dragon": 1,"Tenebres": 2,"Acier": 0.5},
    "Roche": {"Normal": 1, "Feu": 2, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 2, "Combat": 0.5, "Poison": 1 ,"Sol": 0.5,"Vol": 2,"Psy": 1,"Insecte": 2,"Roche": 1,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Spectre": {"Normal": 0, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 2,"Dragon": 1,"Tenebres": 0.5,"Acier": 0.5},
    "Dragon": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 2,"Tenebres": 1,"Acier": 0.5},
    "Tenebres": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Electrik": 1, "Glace": 1, "Combat": 0.5, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 2,"Dragon": 1,"Tenebres": 0.5,"Acier": 0.5},
    "Acier": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 1, "Electrik": 1, "Glace": 2, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 2,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
}

#Classe qui s'occupe des pokemons et de leurs attributs spécifiques#
        
class pokemon():
    def __init__(self,nom,type,PV,attaque,defense,attaque_spe,defense_spe,vitesse,liste_attaques,effet,niveau):
        self.nom = nom
        self.PV = PV
        self.type = type
        self.attaque = attaque
        self.defense = defense
        self.attaque_spe = attaque_spe
        self.defense_spe = defense_spe
        self.vitesse = vitesse
        self.liste_attaques = [attaque.copier_attaques() for attaque in liste_attaques]
        self.effet = []
        self.niveau = niveau
        liste_items = [Dic_items["Potion"],Dic_items["Antidote"],Dic_items["Anti-brulure"],Dic_items["Reveil"],Dic_items["Anti-Para"],Dic_items["Guerison"],Dic_items["Potion-max"],Dic_items["Hyper-potion"],Dic_items["Super-potion"],Dic_items["Total-soin"]]
        self.liste_items = [items.copier_items() for items in liste_items]
        self.stages_stats = { #Niveaux des stats par rapport aux attaques de status#
          "Attaque" : 0,
          "Attaque_spe": 0,
          "Defense": 0,
          "Defense_spe": 0,
          "Vitesse": 0
       }
        self.effet_round_confusion = None
        self.effet_round_sommeil = None
        self.confusion_duree = None
        self.sommeil_duree = None

    #méthode qui affiche le menu spécfique au pokemon qui joue #

    def afficher_menu(self,joueur):
        while True:
         if self != joueur: #si c'est un bot#
            retour = random.randint(1, len(self.liste_attaques))
            return retour
         res = input(f"Que voulez vous faire ?: (Attaquer/Infos/Items/Changer de pokémon)\n> ")
         if res == "Infos":
           print(f"Informations sur les attaques de {self.nom} : ")
           for i, attaque in enumerate(self.liste_attaques, 1):
            print(f">>> {attaque.nom}: Type: {attaque.type},Catégorie: {attaque.categorie},Puissance: {attaque.puissance},Précision: {attaque.precision},PP: {attaque.pp},Priorité: {attaque.priorite},Effet: {attaque.effet}")
           continue
         if res == "Items":
          print("Selection des items")
          for i, items in enumerate(self.liste_items, 1):
            print(f"{i}. {items.nom}: PV: {items.PV_item},PP: {items.PP_item}, quantité: {items.quantite},description: {items.description}")
          choix_item = input()
          if choix_item.isdigit() and 0 < int(choix_item) < len(self.liste_items):
           self.utulisation_item(choix_item)
          else:
           continue
         if res =="Changer de pokémon":
           print("Changement de pokémon")
           choix_pokemon = input()
           if choix_pokemon.isdigit() and 0 < int(choix_pokemon) < len():
              pass
           else:
            continue
         if res == "Attaquer":  
          print(f"Attaques disponibles pour {self.nom} :")
          for i, attaque in enumerate(self.liste_attaques, 1):
            print(f"{i}. {attaque.nom} (Puissance: {attaque.puissance}, PP: {attaque.pp})")
          if self == joueur: #si c'est le joueur qui attaque ou bien c'est un combat entre joueurs#
               retour = int(input())
          while retour > 4 or retour < 1:
             print("Valeur possible depassé veuillez réessayer")
             retour = int(input())
          return retour
         else:
            continue
         
          

   #méthode de calcul du stab#

    def calcul_stab(self,res):
        if isinstance(self.type,tuple): #Cas de double type
           if self.liste_attaques[res - 1].type in self.type:
              return 1.5
        else:
           if self.type == self.liste_attaques[res - 1].type: # Cas un seul type#
              return 1.5
        return 1
           
   #méthode qui gère les coups critiques , leur probabilité et leur multiplicateur#

    def coup_critique(self):
       if random.randint(1, 16) == 1:
        print("Coup Critique !")
        return 2
       else:
        return 1
       
   #méthode qui s'occupe de gérer le multiplicateur des attaques selon le type de l'attaque et du pokemon qui la subit#
       
    def efficacite_type(self,second,res):
       if not isinstance(second.type, tuple): #Permet de savoir si second.type n'est pas un tuple , ducoup si le pokemon a 1 seul type#
         Efficacite = type_dic[self.liste_attaques[res - 1].type][second.type]
       else:
          Efficacite = type_dic[self.liste_attaques[res - 1].type][second.type[0]] * type_dic[self.liste_attaques[res - 1].type][second.type[1]]
       if Efficacite == 4:
          print("C'est Ultra efficace ! Bravo !")
          return Efficacite
       if Efficacite >= 2:
          print("C'est super efficace !")
          return Efficacite
       elif Efficacite == 1:
          return Efficacite
       elif Efficacite == 0.5:
          print("Ce n'est pas très efficace...")
          return Efficacite
       elif Efficacite == 0:
          print("L'attaque n'a pas eu d'effet !,retournez réviser vos tables de type")
          return Efficacite
       
   #méthode qui crée une possibilité que le pokemon attaquant rate#
       
    def miss(self,res,rounds):
       chance = random.randint(1,100)
       for i in range(len(self.effet) - 1,-1,-1):
        if self.effet[i] == "paralysie":
          if chance <= 25:
             print(f"{self.nom} est paralysé , il ne peut attaquer")
             return True
        if self.effet[i] == "sommeil":
          if self.effet_round_sommeil == None:
             self.effet_round_sommeil = rounds
             self.durée_sommeil = random.randint(1,4)
          if rounds - self.effet_round_sommeil < self.durée_sommeil:
             print(f"{self.nom} fait de beaux rêves !")
             return True
          else:
             print(f"{self.nom} se réveille !")
             self.effet.remove("sommeil")
             self.effet_round_sommeil = None
             self.sommeil_duree = None
             self.nom = self.nom.replace("(ZzzzZ)", "")
       if chance <= self.liste_attaques[res - 1].precision:
          return False
       else:
          return True
       
   #méthode principale qui inclut STAB , miss , coups critique , efficacité type , elle calcule les dégats des attaques , gère la perte des PP , la perte des pv de celui qui subit l'attaque#

    def degats(self,second,res,rounds):
       degats = 0
       STAB = self.calcul_stab(res)
       Efficacite = self.efficacite_type(second,res)
       critique = self.coup_critique()
       miss = self.miss(res,rounds)
       if miss == False:
         if self.liste_attaques[res - 1].categorie == "physique":
           degats = int((((((self.niveau * 0.4 + 2) * self.attaque * self.liste_attaques[res - 1].puissance) /  second.defense ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1))) #randon.uniform inclut les valeurs en float##int permet d'arrondir à l"entier inférieur#
           if self.liste_attaques[res - 1].effet != None:
              self.appliquer_un_statut(second,res)
         if self.liste_attaques[res - 1].categorie == "special":
           degats = int((((((self.niveau * 0.4 + 2) * self.attaque_spe * self.liste_attaques[res - 1].puissance) /  second.defense_spe ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1)))
           if self.liste_attaques[res - 1].effet != None:
              self.appliquer_un_statut(second,res)
         if self.liste_attaques[res - 1].categorie == "statut":
            self.statuts_à_niveau(second,res)
            if self.liste_attaques[res - 1].effet != None:
             self.appliquer_un_statut(second,res)
       else:
          print(f"{self.nom} a raté son attaque")
          degats = 0
       second.PV -= degats
       if second.PV < 0:
          second.PV = 0
       self.liste_attaques[res - 1].pp -= 1
       if degats > 0:
          print(f"{self.nom} a infligé {degats} de dégats en utulisant {self.liste_attaques[res - 1].nom} sur {second.nom} qui est à {second.PV} PV, à son tour !")

    def appliquer_un_statut(self,second,res):
         if self.liste_attaques[res - 1].effet[0] == "burn" and random.randint(1,self.liste_attaques[res - 1].effet[1]) == 1:
            if "burn" not in second.effet:
              print(f"{second.nom} a été brulé")
              second.effet.append("burn")
              second.attaque = second.attaque // 2
            if "(brulé)" not in second.nom: #si l'effet est déjà dans le nom#
              second.nom += "(brulé)"
         if self.liste_attaques[res - 1].effet[0] == "poison" and random.randint(1,self.liste_attaques[res - 1].effet[1]) == 1:
               if "poison" not in second.effet:
                 print(f"{second.nom} a été empoisonné")
                 second.effet.append("poison")
               if "(empoisonné)" not in second.nom: 
                second.nom += "(empoisonné)"
         if self.liste_attaques[res - 1].effet[0] == "paralysie" and random.randint(1,self.liste_attaques[res - 1].effet[1]) == 1:
            if "paralysie" not in second.effet:
               print(f"{second.nom} a été paralysé")
               second.effet.append("paralysie")
               second.vitesse = second.vitesse // 4
            if "(paralysé)" not in second.nom: 
              second.nom += "(paralysé)"
         if self.liste_attaques[res - 1].effet[0] == "confusion" and random.randint(1,self.liste_attaques[res - 1].effet[1]) == 1:
            if "confusion" not in second.effet:
               print(f"{second.nom} est confus")
               second.effet.append("confusion")
            if "(confus)" not in second.nom: 
              second.nom += "(confus)"
         if self.liste_attaques[res - 1].effet[0] == "sommeil" and random.randint(1,self.liste_attaques[res - 1].effet[1]) == 1:
            if "sommeil" not in second.effet:
               print(f"{second.nom} a été endormi")
               second.effet.append("sommeil")
            if "(ZzzzZ)" not in second.nom: 
              second.nom += "(ZzzzZ)"

    def remise_niveau(self):
     while True:
        niveau= input(f"De quel niveau est {self.nom} ? (1-100)\n>  ")
        if niveau.isdigit(): #vérifie si c'est un chiffre ou un nombre#
            niveau = int(niveau)
            if 1 <= niveau <= 100:
                break
        print("Valeur incorrecte. Veuillez entrer un nombre entier entre 1 et 100.")

     self.niveau = niveau
     self.PV = (((2 * self.PV) * niveau) // 100) + niveau + 10
     self.attaque = (((2 * self.attaque) * niveau) // 100) + 5
     self.attaque_spe = (((2 * self.attaque_spe) * niveau) // 100) + 5
     self.defense = (((2 * self.defense) * niveau) // 100) + 5
     self.defense_spe = (((2 * self.defense_spe) * niveau) // 100) + 5
     self.vitesse = (((2 * self.vitesse) * niveau) // 100) + 5
     self.nom += f"({self.niveau})"
     self.stats_originales = (self.nom,self.PV, self.attaque, self.attaque_spe, self.defense, self.defense_spe) #stats originales du pokemon sauvegardés dans un tuple#

    def statuts_à_niveau(self,second,res):
        dic_niveaux = {
          -6 : 0.25,
          -5: 2/7,
          -4: 1/3,
          -3: 2/5,
          -2: 1/2,
          -1: 2/3,
           0: 1,
           1: 1.5,
           2: 2,
           3: 2.5,
           4: 3,
           5: 3.5,
           6: 4,
         }

        if self.liste_attaques[res - 1].nom == "Mimi-queue":
           second.stages_stats["Defense"] -= 1
           second.stages_stats["Defense"] = max(-6, second.stages_stats["Defense"]) #éviter que l'on descende en dessous de -6#
           second.defense = second.stats_originales[4] * dic_niveaux[second.stages_stats["Defense"]]
           print(f"La défense de {second.nom} a baissé d'1 cran et est désormais de {second.defense}")
  
        if self.liste_attaques[res - 1].nom == "Rugissement":
           second.stages_stats["Attaque"] -= 1
           second.stages_stats["Attaque"] = max(-6, second.stages_stats["Attaque"]) #éviter que l'on descende en dessous de -6#
           second.attaque = second.stats_originales[2] * dic_niveaux[second.stages_stats["Attaque"]]
           print(f"L'attaque de {second.nom} a baissé d'1 cran et est désormais de {second.attaque}")

        if self.liste_attaques[res - 1].nom == "Plénitude":
           self.stages_stats["Attaque_spe"] += 1
           self.stages_stats["Attaque_spe"] = min(6, self.stages_stats["Attaque_spe"]) #éviter que l'on augmente en haut de 6#
           self.attaque_spe = self.stats_originales[3] * dic_niveaux[self.stages_stats["Attaque_spe"]]
           self.stages_stats["Defense_spe"] += 1
           self.stages_stats["Defense_spe"] = min(6, self.stages_stats["Defense_spe"]) #éviter que l'on augmente en haut de 6#
           self.defense_spe = self.stats_originales[5] * dic_niveaux[self.stages_stats["Defense_spe"]]
           print(f"La défense spéciale et l'attaque spéciale de {self.nom} ont augmentés d'1 niveau")

    def Inventaires(self,pokemon2):
     for item in self.liste_items:
        quantite = input(f"Quelle quantité voulez-vous attribuer à l'objet : {item.nom} ? (Pour les 2 Pokémons)\n> ")
        while not quantite.isdigit():  #Vérifie que l'entrée est un entier positif#
            print("Entrée invalide. Veuillez entrer un nombre entier positif ou nul.")
            quantite = input(f"Quelle quantité voulez-vous attribuer à l'objet : {item.nom} ? (Pour les 2 Pokémons)\n> ")

        quantite = int(quantite)
        item.quantite = quantite  
        for item2 in pokemon2.liste_items:
         if item2.nom == item.nom:
            item2.quantite = quantite
           
    def utulisation_item(self,res):
       if self.liste_items[res - 1].nom == "Potion" and self.liste_items[res - 1].quantite > 0:
          if self.liste_items[res - 1].PV_item + self.PV  > self.stats_originales[1]:
             self.PV = self.stats_originales[1]
          else:
           self.PV += 20
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'une potion permet à {self.nom} de regagner 20 PV , {self.nom} est désormais à {self.PV} PV")

       if self.liste_items[res - 1].nom == "Hyper-potion" and self.liste_items[res - 1].quantite > 0:
          if self.liste_items[res - 1].PV_item + self.PV  > self.stats_originales[1]:
             self.PV = self.stats_originales[1]
          else:
           self.PV += 200
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'une Hyper-potion permet à {self.nom} de regagner 200 PV , {self.nom} est désormais à {self.PV} PV")

       if self.liste_items[res - 1].nom == "Super-Potion" and self.liste_items[res - 1].quantite > 0:
          if self.liste_items[res - 1].PV_item + self.PV  > self.stats_originales[1]:
             self.PV = self.stats_originales[1]
          else:
           self.PV += 50
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'une Super-potion permet à {self.nom} de regagner 50 PV , {self.nom} est désormais à {self.PV} PV")

       if self.liste_items[res - 1].nom == "Guerison" and self.liste_items[res - 1].quantite > 0:
          self.PV = self.stats_originales[1]
          self.liste_items[res - 1].quantite -= 1
          for effet in self.effet[:]:  # copie de la liste
           if effet == "burn":
            self.attaque *= 2
           elif effet == "paralysie":
            self.vitesse *= 4
            self.effet.remove(effet)
          self.nom = self.stats_originales[0]
          print(f"L'utulisation d'un objet de guérison permet à {self.nom} de regagner l'entiereté de ses PV et de supprimer ses effets de statut")

       if self.liste_items[res - 1].nom == "Potion-max" and self.liste_items[res - 1].quantite > 0:
          self.PV = self.stats_originales[1]
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'une potion max permet à {self.nom} de regagner l'entiereté de ses PV")

       if self.liste_items[res - 1].nom == "Total-soin" and self.liste_items[res - 1].quantite > 0:
          self.liste_items[res - 1].quantite -= 1
          for effet in self.effet[:]:  # copie de la liste
           if effet == "burn":
            self.attaque *= 2
           elif effet == "paralysie":
            self.vitesse *= 4
            self.effet.remove(effet)
          self.nom = self.stats_originales[0]
          print(f"L'utulisation d'un total-soin permet à {self.nom} de guérir de tous ses effets de statut")

       if self.liste_items[res - 1].nom == "Antidote" and self.liste_items[res - 1].quantite > 0 and "poison" in self.effet:
          self.effet.remove("poison")
          self.nom = self.nom.replace("(empoisonné)", "")
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'un Antidote permet à {self.nom} de guérir de som empoisonnement")

       if self.liste_items[res - 1].nom == "Anti-brulure" and self.liste_items[res - 1].quantite > 0 and "burn" in self.effet:
          self.effet.remove("burn")
          self.nom = self.nom.replace("(brulé)", "")
          self.liste_items[res - 1].quantite -= 1
          self.attaque = self.attaque * 2
          print(f"L'utulisation d'un Anti-brulure permet à {self.nom} de guérir de sa brulure")

       if self.liste_items[res - 1].nom == "Reveil" and self.liste_items[res - 1].quantite > 0 and "sommeil" in self.effet:
          self.effet.remove("sommeil")
          self.nom = self.nom.replace("(ZzzzZ)", "")
          self.liste_items[res - 1].quantite -= 1
          print(f"L'utulisation d'un réveil permet à {self.nom} de se reveiller")

       if self.liste_items[res - 1].nom == "Anti-Para" and self.liste_items[res - 1].quantite > 0 and "paralysie" in self.effet:
          self.effet.remove("paralysie")
          self.nom = self.nom.replace("(paralysé)", "")
          self.liste_items[res - 1].quantite -= 1
          self.vitesse = self.vitesse * 4
          print(f"L'utulisation d'un Anti-Para permet à {self.nom} de guérir sa paralysie")
       

#Liste des pokémons avec leurs attributs#

Salameche = pokemon(nom= "Salameche",type = "Feu",PV = 39,attaque = 52,defense = 43,attaque_spe = 60,defense_spe = 50,vitesse = 65,liste_attaques = [Dic_attaques["Charge"],Dic_attaques["Griffe"],Dic_attaques["Flammeche"],Dic_attaques["Griffe acier"]],effet = None,niveau = 1)
Carapuce = pokemon( nom= "Carapuce",type = "Eau",PV = 44,attaque = 48,defense = 65,attaque_spe = 50,defense_spe = 64,vitesse = 43,liste_attaques =[Dic_attaques["Charge"],Dic_attaques["Pistolet à O"],Dic_attaques["Ecume"],Dic_attaques["Morsure"]],effet = None,niveau = 1)
Bulbizarre = pokemon( nom= "Bulbizarre",type = "Plante",PV = 45,attaque = 49,defense = 49,attaque_spe = 65,defense_spe = 65,vitesse = 45,liste_attaques =[Dic_attaques["Charge"],Dic_attaques["Fouet lianes"],Dic_attaques["Tranch'herbe"],Dic_attaques["Poudre toxik"]],effet = None,niveau = 1)
Pikachu = pokemon( nom= "Pikachu",type = "Electrik",PV = 35,attaque = 55,defense = 30,attaque_spe = 50,defense_spe = 40,vitesse = 90,liste_attaques =[Dic_attaques["Mimi-queue"],Dic_attaques["Cage éclair"],Dic_attaques["Eclair"],Dic_attaques["Vive attaque"]],effet = None,niveau = 1)
Tarsal = pokemon( nom= "Tarsal",type = "Psy",PV = 28,attaque = 25,defense = 25,attaque_spe = 45,defense_spe = 35,vitesse = 40,liste_attaques =[Dic_attaques["Rugissement"],Dic_attaques["Choc mental"],Dic_attaques["Plénitude"],Dic_attaques["Hypnose"]],effet = None,niveau = 1)

Dic_pokemons = {
   "Salameche": Salameche,
   "Carapuce": Carapuce,
   "Bulbizarre" : Bulbizarre,
   "Pikachu" : Pikachu,
   "Tarsal" : Tarsal
}

