#le pokemon1 correspond au joueur 1 et le pokemon2 au joueur 2#
#le niveau des pokemons est le niveau 1(base)#

from pokemons import Dic_pokemons
from gestion_combat import lancement

Salameche = Dic_pokemons["Salameche"]
Carapuce = Dic_pokemons["Carapuce"]
Bulbizarre = Dic_pokemons["Bulbizarre"]
Pikachu = Dic_pokemons["Pikachu"]
Tarsal = Dic_pokemons["Tarsal"]
Metang = Dic_pokemons["Metang"]
Poussifeu = Dic_pokemons["Poussifeu"]
Gobou = Dic_pokemons["Gobou"]
Arcko = Dic_pokemons["Arcko"]

equipe1 = [Metang,Poussifeu]
equipe2 = [Arcko,Gobou]

if __name__ == "__main__":
  partie = lancement(equipe1,equipe2)
  partie.lancement_combat() 