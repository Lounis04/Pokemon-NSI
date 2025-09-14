#le pokemon1 correspond au joueur 1 et le pokemon2 au joueur 2#
#le niveau des pokemons est le niveau 1(base)#

from pokemons import Dic_pokemons
from gestion_combat import lancement

Salameche = Dic_pokemons["Salameche"]
Carapuce = Dic_pokemons["Carapuce"]
Bulbizarre = Dic_pokemons["Bulbizarre"]
Pikachu = Dic_pokemons["Pikachu"]
Tarsal = Dic_pokemons["Tarsal"]

partie = lancement(Pikachu, Tarsal)
partie.lancement_combat()