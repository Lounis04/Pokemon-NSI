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
Antidote = Items("Antidote",0,0,0,"Soigne les pokémons empoisonnés")
Anti_brule = Items("Anti-brulure",0,0,0,"Soigne les pokémons brulés")
Reveil = Items("Reveil",0,0,0,"Réveille les pokémons endormis")
Anti_para = Items("Anti-Para",0,0,0,"Soigne les pokémons paralysés")


Dic_items = {
    "Potion": Potion,
    "Antidote": Antidote,
    "Anti-brulure": Anti_brule,
    "Reveil": Reveil,
    "Anti-Para": Anti_para
}