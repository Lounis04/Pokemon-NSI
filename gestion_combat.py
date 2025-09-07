import random

#Classe qui s'occupe de la gestion du combat #

class lancement():
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

   #Méthode qui permet de lancer le combat #

    def lancement_combat(self):
        rounds = 1
        print("combat lancé")
        mode = self.choix_mode_jeu() #0 correspond à du joueur contre joueur et 1 du joueur contre bot#
        if mode == 0:
           while self.pokemon1.PV > 0 or self.pokemon2.PV > 0:
             premier = self.joue_en_premier()
             second = self.joue_en_second(premier)
             if rounds == 1:
              print(f" >>>>>>>>>> début du round {rounds}, {premier.nom} commence <<<<<<<<<<<")
             premier.afficher_menu()
             premier.degats(second)
             if second.PV <= 0:  
                print(f"{second.nom} a été vaincu!")
                break
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
             second.afficher_menu() 
             second.degats(premier) 
             if premier.PV <= 0:  
                print(f"{premier.nom} a été vaincu!")
                break
             rounds += 1
             print(f" >>>>>>>>>> début du round {rounds}, {premier.nom} commence <<<<<<<<<<<")
        if mode == 1:
           joueur = self.choix_pokemon_bot()
           while self.pokemon1.PV > 0 or self.pokemon2.PV > 0:
             premier = self.joue_en_premier()
             second = self.joue_en_second(premier)
             print(f">>>>>>>>>>>>> début du round {rounds}, {premier.nom} commence >>>>>>>>>>>>")
             if premier == joueur:
               premier.afficher_menu()
               premier.degats(second)
               print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
               second.degats_bot(premier)
               if second.PV <= 0:
                print(f"{second.nom} a été vaincu !")
                break
             if second == joueur:
              premier.degats_bot(second)
              print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
              second.afficher_menu()
              second.degats(premier)
              if premier.PV <= 0:
               print(f"{premier.nom} a été vaincu !")
               break
             rounds += 1
                 
   #Méthode qui demande le choix du mode de jeu : contre un joueur ou un bot#

    def choix_mode_jeu(self):
        res = input("Voulez-vous jouer contre un joueur ou un bot ? (joueur/bot)\n> ") # \n permet de sauter la ligne pour la réponse  #
        if res == "joueur":
           return 0
        if res == "bot":
           return 1

   #Méthode qui demande au joueur quel pokemon il veut jouer s'il souhaite jouer contre un bot#           

    def choix_pokemon_bot(self):
        res = input(f"lequel des 2 pokemons voulez vous etre le dresseur ?: ({self.pokemon1.nom}/{self.pokemon2.nom})\n> ")
        if res == self.pokemon1.nom:
           print(f"vous êtes désormais le dresseur de : {self.pokemon1.nom}" )
           return self.pokemon1
        if res == self.pokemon2.nom:
           print(f"vous êtes désormais le dresseur de : {self.pokemon2.nom}" )
           return self.pokemon2
        
   #Méthode qui définit qui joue en premier grâce à la vitesse des pokemons#

    def joue_en_premier(self):
       if self.pokemon1.vitesse > self.pokemon2.vitesse:
          return self.pokemon1
       elif self.pokemon1.vitesse < self.pokemon2.vitesse:
          return self.pokemon2
       else:
         return random.choice([self.pokemon1, self.pokemon2]) #Si les deux ont la même vitesse#
       
   #Méthode qui définit qui joue en second par la vitesse#
       
    def joue_en_second(self,premier):
       if premier == self.pokemon1:
          return self.pokemon2
       if premier == self.pokemon2:
          return self.pokemon1
       
            

        


