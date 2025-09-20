class Items():
    def __init__(self,nom,PV_item,PP_item,quantite,description):
        self.nom = nom
        self.PV_item = PV_item
        self.PP_item = PP_item
        self.quantite = quantite
        self.description = description

    def copier_items(self):     
       return Items(
           nom = self.nom,
           PV_item = self.PV_item,
           PP_item = self.PP_item,
           quantite = self.quantite,
           description = self.description
       )

Potion = Items("Potion",20,0,0,"Restaure 20 PV") #La quantité de base pour un item est de 0#
Antidote = Items("Antidote",0,0,0,"Soigne les pokémons empoisonnés(utulisable que si le pokemon a l'effet poison)")
Anti_brule = Items("Anti-brulure",0,0,0,"Soigne les pokémons brulés(utulisable que si le pokemon a l'effet burn)")
Reveil = Items("Reveil",0,0,0,"Réveille les pokémons endormis(utulisable que si le pokemon a l'effet sommeil")
Anti_para = Items("Anti-Para",0,0,0,"Soigne les pokémons paralysés(utulisable que si le pokemon a l'effet paralysie)")
Guerison = Items("Guerison","max",0,0,"Soigne entièrement les pv d'un pokémon et enleve ses effets de statut")
Potion_max = Items("Potion-max",0,0,0,"Soigne entiérement les PV d'un pokémon")
Hyper_potion = Items("Hyper-potion",200,0,0,"Restaure 200 PV")
Super_potion = Items("Super-potion",50,0,0,"Restaure 50 PV")
Total_soin = Items("Total-soin",0,0,0,"Soigne les changements de statut d'un pokémon")


Dic_items = {
    "Potion": Potion,
    "Antidote": Antidote,
    "Anti-brulure": Anti_brule,
    "Reveil": Reveil,
    "Anti-Para": Anti_para,
    "Guerison": Guerison,
    "Potion-max": Potion_max,
    "Hyper-potion": Hyper_potion,
    "Super-potion": Super_potion,
    "Total-soin": Total_soin,
}