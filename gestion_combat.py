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
             if rounds == 1:
              print(f">>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
             print(f"Dresseur de {self.pokemon1.nom} que voulez vous faire ?")
             joueur = self.pokemon1
             res_pokemon1 = self.pokemon1.afficher_menu(joueur)
             print(f"Dresseur de {self.pokemon2.nom} que voulez vous faire ?")
             joueur = self.pokemon2
             res_pokemon2 = self.pokemon2.afficher_menu(joueur) 
             premier = self.joue_en_premier(res_pokemon1,res_pokemon2)
             second = self.joue_en_second(premier)
             self.applications_statut(premier,second)
             print(f">>>>>>>>>> {premier.nom} commence <<<<<<<<<<<")
             if self.pokemon1 == premier:
              premier.degats(second,res_pokemon1)
             else:
              premier.degats(second,res_pokemon2)
             if second.PV <= 0:  
                print(f"{second.nom} a été vaincu!")
                break
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
             if self.pokemon1 == second:
               second.degats(premier,res_pokemon1) 
             else:
                second.degats(premier,res_pokemon2)
             if premier.PV <= 0:  
                print(f"{premier.nom} a été vaincu!")
                break
             rounds += 1
             print(f" >>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
        if mode == 1:
           joueur = self.choix_pokemon_bot()
           if joueur == self.pokemon1:
              bot = self.pokemon2
           else:
              bot = self.pokemon1
           while self.pokemon1.PV > 0 or self.pokemon2.PV > 0:
             print(f"Dresseur de {joueur.nom} que voulez vous faire ?")
             res_joueur = joueur.afficher_menu(joueur)
             res_bot = bot.afficher_menu(joueur)
             premier = self.joue_en_premier(res_joueur,res_bot)
             second = self.joue_en_second(premier)
             self.applications_statut(premier,second)
             print(f">>>>>>>>>>>>> début du round {rounds}, {premier.nom} commence <<<<<<<<<<<")
             if joueur == premier:
              premier.degats(second,res_joueur)
             else:
              premier.degats(second,res_bot)
             if second.PV <= 0:  
                print(f"{second.nom} a été vaincu!")
                break
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
             if joueur == second:
               second.degats(premier,res_joueur) 
             else:
                second.degats(premier,res_bot)
             if premier.PV <= 0:  
                print(f"{premier.nom} a été vaincu!")
             rounds += 1
             print(f" >>>>>>>>>> début du round {rounds} <<<<<<<<<<<")
                 
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

    def joue_en_premier(self,res_pokemon1,res_pokemon2):
       if self.pokemon1.liste_attaques[res_pokemon1 - 1].priorite > self.pokemon2.liste_attaques[res_pokemon2 - 1].priorite:
          return self.pokemon1
       if self.pokemon2.liste_attaques[res_pokemon2 - 1].priorite > self.pokemon1.liste_attaques[res_pokemon1 - 1].priorite:
          return self.pokemon2
       if self.pokemon1.vitesse > self.pokemon2.vitesse:
          return self.pokemon1
       if self.pokemon1.vitesse < self.pokemon2.vitesse:
          return self.pokemon2
       else:
         return random.choice([self.pokemon1, self.pokemon2]) #Si les deux ont la même vitesse#
       
   #Méthode qui définit qui joue en second par la vitesse#
       
    def joue_en_second(self,premier):
       if premier == self.pokemon1:
          return self.pokemon2
       if premier == self.pokemon2:
          return self.pokemon1
       
   #Méthode qui applique les effets des status#

    def applications_statut(self,premier,second):
       if premier.effet == "burn":
          premier.PV -= (premier.PV // 8)
          print(f"{premier.nom} subit les effets de ses brulures et perd {premier.PV // 8} PV, il est désormais à {premier.PV}")
       if second.effet == "burn":
          second.PV -= (second.PV // 8)
          print(f"{second.nom} subit les effets de ses brulures et perd {second.PV // 8} PV, il est désormais à {second.PV}")
       if premier.effet == "poison":
          premier.PV -= (premier.PV // 8)
          print(f"{premier.nom} subit les effets de l'empoisonnement et perd {premier.PV // 8} PV, il est désormais à {premier.PV}")
       if second.effet == "poison":
          second.PV -= (second.PV // 8)
          print(f"{second.nom} subit les effets de l'empoisonnement et perd {second.PV // 8} PV, il est désormais à {second.PV}")
      #Les effets de la paralysie sont pris en compte dans miss()

    def lancement_combat_save(self):
        rounds = 1
        print("combat lancé")
        mode = self.choix_mode_jeu() #0 correspond à du joueur contre joueur et 1 du joueur contre bot#
        if mode == 0:
           while self.pokemon1.PV > 0 or self.pokemon2.PV > 0:
             premier = self.joue_en_premier()
             second = self.joue_en_second(premier)
             self.applications_statut(premier,second)
             if rounds == 1:
              print(f" >>>>>>>>>> début du round {rounds}, {premier.nom} commence <<<<<<<<<<<")
             premier.afficher_menu()
             premier.degats(None,second)
             if second.PV <= 0:  
                print(f"{second.nom} a été vaincu!")
                break
             print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
             second.afficher_menu() 
             second.degats(None,premier) 
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
             self.applications_statut(premier,second)
             print(f">>>>>>>>>>>>> début du round {rounds}, {premier.nom} commence >>>>>>>>>>>>")
             if premier == joueur:
               premier.afficher_menu()
               premier.degats(None,second)
               print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
               second.degats(joueur,premier)
               if second.PV <= 0:
                print(f"{second.nom} a été vaincu !")
                break
             if second == joueur:
              premier.degats(joueur,second)
              print(f">>>>>>>>>> Au tour de {second.nom} <<<<<<<<<<")
              second.afficher_menu()
              second.degats(None,premier)
              if premier.PV <= 0:
               print(f"{premier.nom} a été vaincu !")
               break
             rounds += 1
       

       
       
            

        


