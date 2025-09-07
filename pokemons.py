from attaques import Dic_attaques
import random

#Dictionnaire des types dans pokemon génération 3#
type_dic = {
    "Normal": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 1, "Combat": 2, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 0.5,"Spectre": 0,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Feu": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 2, "Électrik": 1, "Glace": 2, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 2,"Roche": 0.5,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 2},
    "Eau": {"Normal": 1, "Feu": 2, "Eau": 0.5, "Plante": 0.5, "Électrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 2,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 2,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 1},
    "Plante": {"Normal": 1, "Feu": 0.5, "Eau": 2, "Plante": 0.5, "Électrik": 1, "Glace": 1, "Combat": 1, "Poison": 0.5 ,"Sol": 2,"Vol": 0.5,"Psy": 1,"Insecte": 0.5,"Roche": 2,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 0.5},
    "Electrik": {"Normal": 1, "Feu": 1, "Eau": 2, "Plante": 0.5, "Électrik": 0.5, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 0,"Vol": 2,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 0.5,"Tenebres": 1,"Acier": 1},
    "Glace": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 2, "Électrik": 1, "Glace": 0.5, "Combat": 1, "Poison": 1 ,"Sol": 2,"Vol": 2,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 2,"Tenebres": 1,"Acier": 0.5},
    "Combat": {"Normal": 2, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 2, "Combat": 1, "Poison": 0.5 ,"Sol": 1,"Vol": 0.5,"Psy": 0.5,"Insecte": 0.5,"Roche": 2,"Spectre": 0,"Dragon": 1,"Tenebres": 2,"Acier": 2},
    "Poison": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 2, "Électrik": 1, "Glace": 1, "Combat": 1, "Poison": 0.5 ,"Sol": 0.5,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 0.5,"Spectre": 0.5,"Dragon": 1,"Tenebres": 1,"Acier": 0},
    "Sol": {"Normal": 1, "Feu": 2, "Eau": 1, "Plante": 0.5, "Électrik": 2, "Glace": 1, "Combat": 1, "Poison": 2 ,"Sol": 1,"Vol": 0,"Psy": 1,"Insecte": 0.5,"Roche": 2,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 2},
    "Vol": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 2, "Électrik": 0.5, "Glace": 1, "Combat": 2, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 2,"Roche": 0.5,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Psy": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 1, "Combat": 2, "Poison": 2 ,"Sol": 1,"Vol": 1,"Psy": 0.5,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 1,"Tenebres": 0,"Acier": 0.5},
    "Insecte": {"Normal": 1, "Feu": 0.5, "Eau": 1, "Plante": 2, "Électrik": 1, "Glace": 1, "Combat": 0.5, "Poison": 0.5 ,"Sol": 1,"Vol": 0.5,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 0.5,"Dragon": 1,"Tenebres": 2,"Acier": 0.5},
    "Roche": {"Normal": 1, "Feu": 2, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 2, "Combat": 0.5, "Poison": 1 ,"Sol": 0.5,"Vol": 2,"Psy": 1,"Insecte": 2,"Roche": 1,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
    "Spectre": {"Normal": 0, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 2,"Dragon": 1,"Tenebres": 0.5,"Acier": 0.5},
    "Dragon": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 1, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 1,"Spectre": 1,"Dragon": 2,"Tenebres": 1,"Acier": 0.5},
    "Tenebres": {"Normal": 1, "Feu": 1, "Eau": 1, "Plante": 1, "Électrik": 1, "Glace": 1, "Combat": 0.5, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 2,"Insecte": 1,"Roche": 1,"Spectre": 2,"Dragon": 1,"Tenebres": 0.5,"Acier": 0.5},
    "Acier": {"Normal": 1, "Feu": 0.5, "Eau": 0.5, "Plante": 1, "Électrik": 1, "Glace": 2, "Combat": 1, "Poison": 1 ,"Sol": 1,"Vol": 1,"Psy": 1,"Insecte": 1,"Roche": 2,"Spectre": 1,"Dragon": 1,"Tenebres": 1,"Acier": 0.5},
}


#Classe qui s'occupe des pokemons et de leurs attributs spécifiques#
        
class pokemon():
    def __init__(self,nom,type,PV,attaque,defense,attaque_spe,defense_spe,vitesse,liste_attaques):
        self.nom = nom
        self.PV = PV
        self.type = type
        self.attaque = attaque
        self.defense = defense
        self.attaque_spe = attaque_spe
        self.defense_spe = defense_spe
        self.vitesse = vitesse
        self.liste_attaques = [attaque.copier() for attaque in liste_attaques] 

    #méthode qui affiche le menu spécfique au pokemon qui joue #

    def afficher_menu(self):
        print(f"Attaques disponibles pour {self.nom} :")
        for i, attaque in enumerate(self.liste_attaques, 1):
            print(f"{i}. {attaque.nom} (Puissance: {attaque.puissance}, PP: {attaque.pp})")

   #méthode de calcul du stab#

    def calcul_stab(self,res):
       if self.type == self.liste_attaques[res - 1].type:
          STAB = 1.5
       else:
          STAB = 1
       return STAB

   #méthode qui gère les coups critiques , leur probabilité et leur multiplicateur#

    def coup_critique(self):
       if random.randint(1, 16) == 1:
        print("Coup Critique !")
        return 2
       else:
        return 1
       
   #méthode qui s'occupe de gérer le multiplicateur des attaques selon le type de l'attaque et du pokemon qui la subit#
       
    def efficacite_type(self,second,res):
       Efficacite = type_dic[self.liste_attaques[res - 1].type][second.type]
       if Efficacite == 2:
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
       
    def miss(self,res):
       chance = random.randint(1,100)
       if chance <= self.liste_attaques[res - 1].precision:
          return False
       else:
          return True
       
   #méthode principale qui inclut STAB , miss , coups critique , efficacité type , elle calcule les dégats des attaques , gère la perte des PP , la perte des pv de celui qui subit l'attaque#

    def degats(self,second):
       res = int(input())
       if res > 4:
        print("Valeur possible depassé veuillez réessayer")
        res = int(input())
       STAB = self.calcul_stab(res)
       Efficacite = self.efficacite_type(second,res)
       critique = self.coup_critique()
       miss = self.miss(res)
       if miss == False:
         if self.liste_attaques[res - 1].categorie == "physique":
           degats = int(((((2.4 * self.attaque * self.liste_attaques[res - 1].puissance) /  second.defense ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1))) #randon.uniform inclut les valeurs en float##int permet d'arrondir à l"entier inférieur#
         if self.liste_attaques[res - 1].categorie == "special":
           degats = int(((((2.4 * self.attaque_spe * self.liste_attaques[res - 1].puissance) /  second.defense_spe ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1)))
       else:
          print(f"{self.nom} a raté son attaque")
          degats = 0
       second.PV -= degats
       if second.PV < 0:
          second.PV = 0
       self.liste_attaques[res - 1].pp -= 1
       print(f"{self.nom} a infligé {degats} de dégats à {second.nom} qui est à {second.PV} PV, à son tour !")

#méthode qui calcule les dégats pour le bot#

    def degats_bot (self,second):
       res = random.randint(1, len(self.liste_attaques))
       STAB = self.calcul_stab(res)
       Efficacite = self.efficacite_type(second,res)
       critique = self.coup_critique()
       miss = self.miss(res)
       if miss == False:
         if self.liste_attaques[res - 1].categorie == "physique":
           degats = int(((((2.4 * self.attaque * self.liste_attaques[res - 1].puissance) /  second.defense ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1))) #randon.uniform inclut les valeurs en float##int permet d'arrondir à l"entier inférieur#
         if self.liste_attaques[res - 1].categorie == "special":
           degats = int(((((2.4 * self.attaque_spe * self.liste_attaques[res - 1].puissance) /  second.defense_spe ) / 50 ) + 2) * (STAB * Efficacite * critique * random.uniform(0.85,1)))
       else:
          print(f"{self.nom} a raté son attaque")
          degats = 0
       second.PV -= degats
       if second.PV < 0:
          second.PV = 0
       self.liste_attaques[res - 1].pp -= 1
       print(f"{self.nom} a infligé {degats} de dégats à {second.nom} qui est à {second.PV} PV, à son tour !")


#Liste des pokémons avec leurs attributs#

Salameche = pokemon(
   nom= "Salameche",
   type = "Feu",
   PV = 39,
   attaque = 52,
   defense = 43,
   attaque_spe = 60,
   defense_spe = 50,
   vitesse = 65,
   liste_attaques = [Dic_attaques["Charge"],Dic_attaques["Griffe"],Dic_attaques["Flammeche"],Dic_attaques["Griffe acier"]])

Carapuce = pokemon(
   nom= "Carapuce",
   type = "Eau",
   PV = 44,
   attaque = 48,
   defense = 65,
   attaque_spe = 50,
   defense_spe = 64,
   vitesse = 43,
   liste_attaques =[Dic_attaques["Charge"],Dic_attaques["Pistolet à O"],Dic_attaques["Ecume"],Dic_attaques["Morsure"]])

Dic_pokemons = {
   "Salameche": Salameche,
   "Carapuce": Carapuce
}