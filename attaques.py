
class Attaques:
    "Initialisation de la classe Attaques ,on prend tous ses attributs en entrée et on les intégre à la classe"
    def __init__(self,nom: str,type: str,categorie: str,puissance: int | None,precision: int,pp: int,priorite: int,effet: tuple[str, int] | None) -> None:
        self.nom: str = nom
        self.type: str = type
        self.categorie: str = categorie
        self.puissance: int | None = puissance
        self.precision: int = precision
        self.pp: int = pp
        self.priorite: int = priorite
        self.effet: tuple[str, int] | None = effet

    def copier_attaques(self) -> "Attaques":
        "Méthode qui permet de créer une copie des attaques ,ceci permet d'éviter la globalisation des élements des attaques entre les pokémons (PP,etc,..),Elle prend en entrée"
        "tous les arguments de la classe et en resort des copies , elle est utulisée dans l'init de la classe Pokémon"
        return Attaques(
            nom=self.nom,
            type=self.type,
            categorie=self.categorie,
            puissance=self.puissance,
            precision=self.precision,
            pp=self.pp,
            priorite=self.priorite,
            effet=self.effet,
        )

#Liste des attaques avec leurs attributs#

Charge: Attaques = Attaques("Charge", "Normal", "physique", 35, 95, 35, 0, None)
Griffe: Attaques = Attaques("Griffe", "Normal", "physique", 40, 100, 35, 0, None)
Flammeche: Attaques = Attaques("Flammeche", "Feu", "special", 40, 100, 25, 0, ("burn", 8))
Griffe_acier: Attaques = Attaques("Griffe acier", "Acier", "physique", 50, 95, 35, 0, None)
Pistolet_A_O: Attaques = Attaques("Pistolet à O", "Eau", "special", 40, 100, 25, 0, None)
Ecume: Attaques = Attaques("Ecume", "Eau", "special", 20, 100, 30, 0, None)
Morsure: Attaques = Attaques("Morsure", "Tenebres", "special", 60, 100, 25, 0, None)
Fouet_lianes: Attaques = Attaques("Fouet liane", "Plante", "special", 45, 100, 25, 0, None)
Tranch_herbe: Attaques = Attaques("Tranch'herbe", "Plante", "special", 55, 95, 25, 0, None)
Poudre_toxik: Attaques = Attaques("Poudre toxik", "Poison", "statut", None, 75, 35, 0, ("poison", 1))
Cage_eclair: Attaques = Attaques("Cage éclair", "Electrik", "statut", None, 100, 20, 0, ("paralysie", 1))
Eclair: Attaques = Attaques("Eclair", "Electrik", "special", 40, 100, 30, 0, ("paralysie", 10))
Vive_attaque: Attaques = Attaques("Vive attaque", "Normal", "physique", 40, 100, 30, 1, None)
Mimi_queue: Attaques = Attaques("Mimi-queue", "Normal", "statut", 0, 100, 30, 0, None)
Rugissement: Attaques = Attaques("Rugissement", "Normal", "statut", 0, 100, 10, 0, None)
Choc_mental: Attaques = Attaques("Choc mental", "Psy", "special", 50, 100, 25, 0, ("confusion", 1))
Plénitude: Attaques = Attaques("Plénitude", "Psy", "statut", 0, 100, 20, 0, None)
Hypnose: Attaques = Attaques("Hypnose", "Psy", "statut", 0, 60, 20, 0, ("sommeil", 1))
Meteores: Attaques = Attaques("Meteores", "Normal", "special", 60, 100, 20, 0, None)
Double_Pied: Attaques = Attaques("Double-Pied", "Combat", "physique", 30, 100, 30, 0, None)
Psyko: Attaques = Attaques("Psyko", "Psy", "special", 90, 100, 10, 0, ("confusion", 10))
Poing_Meteore: Attaques = Attaques("Poing Météore", "Acier", "physique", 90, 90, 10, 0, None)


# Dictionnaire des attaques avec l'attaque et sa clé associée#

Dic_attaques: dict[str, Attaques] = {
    "Charge": Charge,
    "Griffe": Griffe,
    "Flammeche": Flammeche,
    "Griffe acier": Griffe_acier,
    "Pistolet à O": Pistolet_A_O,
    "Ecume": Ecume,
    "Morsure": Morsure,
    "Fouet lianes": Fouet_lianes,
    "Tranch'herbe": Tranch_herbe,
    "Poudre toxik": Poudre_toxik,
    "Cage éclair": Cage_eclair,
    "Eclair": Eclair,
    "Vive attaque": Vive_attaque,
    "Mimi-queue": Mimi_queue,
    "Rugissement": Rugissement,
    "Choc mental": Choc_mental,
    "Plénitude": Plénitude,
    "Hypnose": Hypnose,
    "Meteores": Meteores,
    "Poing Meteore": Poing_Meteore,
    "Psyko": Psyko,
    "Double-Pied": Double_Pied,
}
