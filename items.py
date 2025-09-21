class Items():
    def __init__(self,nom,PV_item,PP_item,quantite,description,boosts):
        self.nom = nom
        self.PV_item = PV_item
        self.PP_item = PP_item
        self.quantite = quantite
        self.description = description
        self.boosts = boosts or {}  # Exemple : {"attaque": +10, "defense": +5}

    def copier_items(self):     
        return Items(
           nom = self.nom,
           PV_item = self.PV_item,
           PP_item = self.PP_item,
           quantite = self.quantite,
           description = self.description,
           boosts = self.boosts)

Potion = Items("Potion",20,0,0,"Restaure 20 PV",None) #La quantité de base pour un item est de 0#
Antidote = Items("Antidote",0,0,0,"Soigne les pokémons empoisonnés(utulisable que si le pokemon a l'effet poison)",None)
Anti_brule = Items("Anti-brulure",0,0,0,"Soigne les pokémons brulés(utulisable que si le pokemon a l'effet burn)",None)
Reveil = Items("Reveil",0,0,0,"Réveille les pokémons endormis(utulisable que si le pokemon a l'effet sommeil",None)
Anti_para = Items("Anti-Para",0,0,0,"Soigne les pokémons paralysés(utulisable que si le pokemon a l'effet paralysie)",None)
Anti_gel = Items("Anti-gel",0,0,0,"Soigne les pokémons gelés(utulisable que si le pokemon a l'effet gelés)",None)
Guerison = Items("Guerison","max",0,0,"Soigne entièrement les pv d'un pokémon et enleve ses effets de statut",None)
Potion_max = Items("Potion-max",0,0,0,"Soigne entiérement les PV d'un pokémon",None)
Hyper_potion = Items("Hyper-potion",200,0,0,"Restaure 200 PV",None)
Super_potion = Items("Super-potion",50,0,0,"Restaure 50 PV",None)
Total_soin = Items("Total-soin",0,0,0,"Soigne les changements de statut d'un pokémon",None)
Rappel = Items("Rappel","max",0,0,"Réanime un pokémon mort avec la moitié de ses PV",None)
Rappel_max = Items("Rappel max","moitié des pv",0,0,"Réanime une pokémon mort avec l'entiereté de ses PV",None)
Proteine = Items("Protéine",0,0,0,"Baie qui augmente l'attaque de 10",{"attaque": 10})
Fer = Items("Fer",0,0,0,"Augmente la défense de 10 points",{"defense": 10})
PV_plus = Items("PV plus",0,0,0,"Augmente la défense de 10 points",{"PV": 10})


Dic_items = {
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

Dic_items_tenus = {
    "Protéine": Proteine,
    "Fer": Fer,
    "PV plus": PV_plus
    }