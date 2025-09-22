#Bienvenue dans le simulateur de combat de pokémon , afin de changer les équipes il faut changer les élements des listes equipe1 et equipe#

from pokemons import Dic_pokemons
from gestion_combat import lancement

#Association au pokémon à sa clé dans le dictionnaire des pokémons Dic_pokemons#

Salameche = Dic_pokemons["Salameche"]
Carapuce = Dic_pokemons["Carapuce"]
Bulbizarre = Dic_pokemons["Bulbizarre"]
Pikachu = Dic_pokemons["Pikachu"]
Tarsal = Dic_pokemons["Tarsal"]
Metang = Dic_pokemons["Metang"]
Poussifeu = Dic_pokemons["Poussifeu"]
Gobou = Dic_pokemons["Gobou"]
Arcko = Dic_pokemons["Arcko"]

#Liste des équipes#
#Pokémons disponibles : Salameche , Carapuce , Bulbizarre , Pikachu , Tarsal , Métang(trop abusé lui) , Poussifeu , Gobou , Arcko#

equipe1: list = [Carapuce,Pikachu]
equipe2: list = [Tarsal,Metang]

#Lancement du combat avec la classe principale lancement_combat#

if __name__ == "__main__":
  partie = lancement(equipe1,equipe2)
  partie.lancement_combat() 