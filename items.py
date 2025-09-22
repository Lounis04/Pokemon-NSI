class Items():
    "Initialisation de la classe Items , elle prend en argument les attributs et les intègre"
    def __init__(self,nom : str ,PV_item : int ,PP_item : int ,quantite : int ,description : str ):
        self.nom : str = nom
        self.PV_item : int = PV_item
        self.PP_item : int = PP_item
        self.quantite : int  = quantite
        self.description : str  = description

    def copier_items(self) -> "Items":
        "Méthode qui crée des copies des items pour éviter de les globaliser(comme les attaques),Elle prend en argument tous les attributs de sa classe et en renvoie une copie , elle est utulisée dans"
        "initialiser_inventaires() et objets_tenus()"
        return Items(
           nom = self.nom,
           PV_item = self.PV_item,
           PP_item = self.PP_item,
           quantite = self.quantite,
           description = self.description,
           )
    
#Liste des items/items_tenus avec leurs attributs#

Potion = Items("Potion",20,0,0,"Restaure 20 PV") #La quantité de base pour un item est de 0#
Antidote = Items("Antidote",0,0,0,"Soigne les pokémons empoisonnés(utulisable que si le pokemon a l'effet poison)")
Anti_brule = Items("Anti-brulure",0,0,0,"Soigne les pokémons brulés(utulisable que si le pokemon a l'effet burn)")
Reveil = Items("Reveil",0,0,0,"Réveille les pokémons endormis(utulisable que si le pokemon a l'effet sommeil")
Anti_para = Items("Anti-Para",0,0,0,"Soigne les pokémons paralysés(utulisable que si le pokemon a l'effet paralysie)")
Anti_gel = Items("Anti-gel",0,0,0,"Soigne les pokémons gelés(utulisable que si le pokemon a l'effet gelé)")
Guerison = Items("Guerison","max",0,0,"Soigne entièrement les pv d'un pokémon et enleve ses effets de statut")
Potion_max = Items("Potion-max",0,0,0,"Soigne entiérement les PV d'un pokémon")
Hyper_potion = Items("Hyper-potion",200,0,0,"Restaure 200 PV")
Super_potion = Items("Super-potion",50,0,0,"Restaure 50 PV")
Total_soin = Items("Total-soin",0,0,0,"Soigne les changements de statut d'un pokémon")
Rappel = Items("Rappel","max",0,0,"Réanime un pokémon mort avec la moitié de ses PV")

Rappel_max = Items("Rappel max","moitié des pv",0,0,"Réanime une pokémon mort avec l'entiereté de ses PV")
Proteine = Items("Protéine",0,0,0,"Baie qui augmente l'attaque de 10")
Fer = Items("Fer",0,0,0,"Augmente la défense de 10 points")
PV_plus = Items("PV plus",0,0,0,"Augmente la défense de 10 points")

#Dictionnaire des items de base#

Dic_items: dict[str, Items] = {
    "Potion": Potion,
    "Antidote": Antidote,
    "Anti-brulure": Anti_brule,
    "Reveil": Reveil,
    "Anti-Para": Anti_para,
    "Anti-gel": Anti_gel,
    "Guerison": Guerison,
    "Potion-max": Potion_max,
    "Hyper-potion": Hyper_potion,
    "Super-potion": Super_potion,
    "Total-soin": Total_soin,
    "Rappel": Rappel,
    "Rappel max": Rappel_max
}

#Dictionnaire des items que les pokémons peuvent équiper#

Dic_items_tenus: dict[str, Items] = {
    "Protéine": Proteine,
    "Fer": Fer,
    "PV plus": PV_plus
    }