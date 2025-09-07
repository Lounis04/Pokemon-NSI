
#Classe qui s'occupe des attaques et de leurs attributs#

class Attaques():
   def __init__(self, nom, type , categorie, puissance, precision, pp, priorite, effet):
        self.nom = nom
        self.type = type
        self.categorie = categorie  
        self.puissance = puissance
        self.precision = precision
        self.pp = pp
        self.priorite = priorite
        self.effet = effet 

   # méthode qui crée une copie des attaques spécifiques aux pokemons pour éviter la globalisation des PP,ceci permet d'éviter par exemple que quand pokemon1 utulise charge alors pokemon2 perd 1 PP de charge aussi#

   def copier(self):     
       return Attaques(
           nom=self.nom,
           type=self.type,
           categorie=self.categorie,
           puissance=self.puissance,
           precision=self.precision,
           pp=self.pp,
           priorite=self.priorite,
           effet=self.effet
       )

#Liste des attaques avec leurs attributs"

Charge = Attaques(
    nom= "Charge",
    type = "Normal",
    categorie= "physique",
    puissance= 35,
    precision= 95,
    pp= 35,
    priorite = 0,
    effet = None
)

Griffe = Attaques(
    nom= "Griffe",
    type = "Normal",
    categorie= "physique",
    puissance= 40,
    precision= 100,
    pp= 35,
    priorite = 0,
    effet = None
)

Flammeche = Attaques(
    nom= "Flammeche",
    type = "Feu",
    categorie= "special",
    puissance= 40,
    precision= 100,
    pp= 25,
    priorite = 0,
    effet = None
)

Griffe_acier = Attaques(
    nom= "Griffe acier",
    type = "Acier",
    categorie= "physique",
    puissance= 50,
    precision= 95,
    pp= 35,
    priorite = 0,
    effet = None
)

Pistolet_A_O = Attaques(
    nom= "Pistolet à O",
    type = "Eau",
    categorie= "special",
    puissance= 40,
    precision= 100,
    pp= 25,
    priorite = 0,
    effet = None
)

Ecume = Attaques(
    nom= "Ecume",
    type = "Eau",
    categorie= "special",
    puissance= 20,
    precision= 100,
    pp= 30,
    priorite = 0,
    effet = None
)

Morsure = Attaques(
    nom= "Morsure",
    type = "Tenebres",
    categorie= "special",
    puissance= 60,
    precision= 100,
    pp= 25,
    priorite = 0,
    effet = None
)

#Dictionnaire des attaques#

Dic_attaques = {"Charge":Charge,
                "Griffe":Griffe,
                "Flammeche":Flammeche,
                "Griffe acier":Griffe_acier,
                "Pistolet à O":Pistolet_A_O,
                "Ecume": Ecume,
                "Morsure": Morsure
                }