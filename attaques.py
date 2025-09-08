
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

Charge = Attaques(nom= "Charge",type = "Normal",categorie= "physique",puissance= 35,precision= 95,pp= 35,priorite =0,effet = None)              
Griffe = Attaques(nom= "Griffe",type = "Normal",categorie= "physique",puissance= 40,precision= 100,pp= 35,priorite = 0,effet = None)
Flammeche = Attaques(nom= "Flammeche",type = "Feu",categorie= "special",puissance= 40,precision= 100,pp= 25,priorite = 0,effet = ("burn",8))     #Pour un effet on prend son nom et sa probabilité , ici 8 correspond à une probabilité de 1/8#
Griffe_acier = Attaques(nom= "Griffe acier",type = "Acier",categorie= "physique",puissance= 50,precision= 95,pp= 35,priorite = 0,effet = None)
Pistolet_A_O = Attaques(nom= "Pistolet à O",type = "Eau",categorie= "special",puissance= 40,precision= 100,pp= 25,priorite = 0,effet = None)
Ecume = Attaques(nom= "Ecume",type = "Eau",categorie= "special",puissance= 20,precision= 100,pp= 30,priorite = 0,effet = None)
Morsure = Attaques(nom= "Morsure",type = "Tenebres",categorie= "special",puissance= 60,precision= 100,pp= 25,priorite = 0,effet = None)
Fouet_lianes = Attaques(nom= "Fouet liane",type = "Plante",categorie= "special",puissance= 45,precision= 100,pp= 25,priorite = 0,effet = None)
Tranch_herbe = Attaques(nom= "Tranch'herbe",type = "Plante",categorie= "special",puissance= 55,precision= 95,pp= 25,priorite = 0,effet = None)
Poudre_toxik = Attaques(nom= "Poudre toxik",type = "Poison",categorie= "statut",puissance= None,precision= 75,pp= 35,priorite = 0,effet = ("poison",1))
Cage_eclair = Attaques(nom= "Cage éclair",type = "Electrik",categorie= "statut",puissance= None,precision= 100,pp= 20,priorite = 0,effet = ("paralysie",1))
Eclair = Attaques(nom= "Eclair",type = "Electrik",categorie= "special",puissance= 40,precision= 100,pp= 30,priorite = 0,effet = ("paralysie",10))
Vive_attaque = Attaques(nom= "Vive attaque",type = "Normal",categorie= "physique",puissance= 40,precision= 100,pp= 30,priorite = 1,effet = None)




#Dictionnaire des attaques#

Dic_attaques = {"Charge":Charge,
                "Griffe":Griffe,
                "Flammeche":Flammeche,
                "Griffe acier":Griffe_acier,
                "Pistolet à O":Pistolet_A_O,
                "Ecume": Ecume,
                "Morsure": Morsure,
                "Fouet lianes": Fouet_lianes,
                "Tranch'herbe": Tranch_herbe,
                "Poudre toxik": Poudre_toxik,
                "Cage éclair": Cage_eclair,
                "Eclair" : Eclair,
                "Vive attaque": Vive_attaque
                }