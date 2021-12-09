from turtle import*
import turtle
import time
import random
from listes import *
import sys
from bonhomme import *
from vlc import vlc

#L'écran du jeu prend la taille de l'écran turtle
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

#Une musique de fond avec le module vlc
player = vlc.MediaPlayer("sounds\music-background.wav")
player.play()

#Pour mettre une couleur de fond
turtle.Screen().bgcolor("#26ABFF")

#Ecran de demarrage
turtle.write("Le jeu du pendu !", align="center", font=("Times New Roman", 60, "normal"))
time.sleep(3)  
turtle.clear()  

#L'utilisateur choisit un niveau
turtle.write("Choisissez votre mode dans la console : \n Tapez 1 pour le mode facile : des mots de 5 lettres à deviner en 12 essais \n Tapez 2 pour le mode moyen : des mots de 8 lettres à deviner en 8 essais \n Tapez 3 pour le mode difficile : des mots de 10 lettres à deviner en 5 essais", align="center",font=("Times",25,"normal"))
modes = int(input("Entrez ici le niveau : "))

#Fonction qui choisit le mot à deviner en fonction du niveau
def mode(modes):
  """"La fonction mode permet de choisir le mot à deviner en fonction du niveau choisi par l'utilisateur. Trois listes sont créées dans le fichier listes.py correspondantes à chaque niveau"""
  global mot #comme vu avec le prof permet de définir mot sur tous le prog
  if modes==1:
    mot=random.choice(liste_facile)
  if modes==2:
    mot=random.choice(liste_moy)
  if modes==3:
    mot=random.choice(liste_dif)

mode(modes) #On exécute la fonction mode

turtle.clear() #pour supprimer l'affichage du choix des niveaux

#On initialise toutes nos variables

lettre_vrai=0 #Qui permet de compter le nombre de lettre juste trouvée

erreur = 0 #Compteur d'erreur, on l'initialise à zéro

l_tirets = [] #La liste à qui on associe les tirets et qu'on remplace par les lettres trouvées

l_utilises = [] #La liste qui permet de vérifier que la lettre entrée n'est pas déjà utilisées

arrangeur=0 #Cette variable permet d'arranger le problème qui suit : Lorsqu'une lettre déjà entrée appartient au mot à trouver, cela modifie la variable lettre_vrai et fait gagner l'utilisateur avant d'avoir toutes les lettres

y=270 #Coordonnée qui sera modifié au cours du programme

mot=list(mot) 
#On convertir le mot en liste pour comparer ses caractères

#Si le niveau 1 est choisi :
if modes == 1 :
  turtle.Screen().bgcolor("#97CF8A")
  
  while erreur!=12:
      
    #On crée une liste avec autant de tirets que de lettre dans le mot à deviner

    l_tirets=["_"]*len(mot)
    lettre_entre = input("Entrez une lettre : ")
    lettre_entre = lettre_entre.upper() #On met la lettre en majuscule pour éviter toute erreur
    pu()
    goto(0,0)
    pd()
    pu()
    goto(460,260)
    pd()
    turtle.write("Lettres utilisées : ", align="center",font=("Times",27,"normal"))

    #On vérifie que la lettre entrée n'est pas déjà utilisé
    
    if lettre_entre in l_utilises:
        
      print("Vous avez déjà entré cette lettre !!!")
      arrangeur=mot.count(lettre_entre)
      
      if lettre_entre in mot:
          
        lettre_vrai-=arrangeur
        
    else:
        
      pu()
      goto(650,y)
      pd()
      turtle.write(lettre_entre, font=("Times",18,"bold"))
      y-=40

    #On vérifie que la lettre entrée n'est pas un chiffre ou un caractère spécial
    
    if lettre_entre not in liste_alp:
        
      print("Vous ne pouvez pas entrer de lettres à caractères spéciaux (sauf les accents) ou plusieurs lettres à la fois !")
    
    else :
        
      fois = mot.count(lettre_entre)
      l_utilises = l_utilises + list(lettre_entre)

  #On compare la lettre entrée à toutes les lettres du mot pour voir si elle correspond

      for i in range(len(mot)):

        if lettre_entre==mot[i]:
            
          pu()
          goto(0,0)
          pd()
          l_tirets[i]=lettre_entre
          lettre_vrai+=1
          player = vlc.MediaPlayer("sounds\letter_found.wav")
          player.play()

  #Si il y a autant de lettres trouvées qu'il y a de lettre dans le mot, c'est gagné !

      winning(lettre_vrai, mot)

  #Si la lettre n'est présente aucune fois dans le mot, c'est une erreur :
      if fois==0:
          
        player = vlc.MediaPlayer("sounds\error.wav")
        player.play()
        erreur+=1
        turtle.width(4)
        bonhomme_1(erreur)
        
    pu()
    goto(0,0)
    pd()
    l_tirets=" ".join(l_tirets) #On convertit l_tirets en str pour l'écrire
    turtle.write(l_tirets, align="center", font=("Times", 40, "bold"))

#Si le niveau 2 est choisi :
if modes == 2 :
  turtle.Screen().bgcolor("#FFAF7A")
  
  while erreur!=8:

    l_tirets=["_"]*len(mot)
    lettre_entre = input("Entrez une lettre : ")
    lettre_entre = lettre_entre.upper()
    pu()
    goto(0,0)
    pd()
    pu()
    goto(460,260)
    pd()
    turtle.write("Lettres utilisées : ", align="center",font=("Times",27,"normal"))
    
    if lettre_entre in l_utilises:
        
      print("Vous avez déjà entré cette lettre !!!")
      arrangeur=mot.count(lettre_entre)
     
      if lettre_entre in mot:
          
        lettre_vrai-=arrangeur
    
    else:
      pu()
      goto(650,y)
      pd()
      turtle.write(lettre_entre, font=("Times",18,"bold"))
      y-=40
    
    if lettre_entre not in liste_alp:
        
      print("Vous ne pouvez pas entrer de lettres à caractères spéciaux (sauf les accents) ou plusieurs lettres à la fois !")
    
    else :
        
      fois = mot.count(lettre_entre)
      l_utilises = l_utilises + list(lettre_entre)

      for i in range(len(mot)):

        if lettre_entre==mot[i]:
            
          pu()
          goto(0,0)
          pd()
          l_tirets[i]=lettre_entre
          lettre_vrai+=1
          player = vlc.MediaPlayer("sounds\letter_found.wav")
          player.play()

      winning(lettre_vrai, mot)

      if fois==0:
          
        player = vlc.MediaPlayer("sounds\error.wav")
        player.play()
        erreur+=1
        turtle.width(4)
        bonhomme_2(erreur)
        
    pu()
    goto(0,0)
    pd()
    l_tirets=" ".join(l_tirets)
    turtle.write(l_tirets, align="center", font=("Times", 40, "bold"))

#Si le niveau 3 est choisi :
if modes == 3 :
  turtle.Screen().bgcolor("#F28B88")
  
  while erreur!=5:

    l_tirets=["_"]*len(mot)
    lettre_entre = input("Entrez une lettre : ")
    lettre_entre = lettre_entre.upper()
    pu()
    goto(0,0)
    pd()
    pu()
    goto(460,260)
    pd()
    turtle.write("Lettres utilisées : ", align="center",font=("Times",27,"normal"))
    
    if lettre_entre in l_utilises:
        
      print("Vous avez déjà entré cette lettre !!!")
      arrangeur=mot.count(lettre_entre)
     
      if lettre_entre in mot:
          
        lettre_vrai-=arrangeur
    
    else:
      pu()
      goto(650,y)
      pd()
      turtle.write(lettre_entre, font=("Times",18,"bold"))
      y-=40
    
    if lettre_entre not in liste_alp:
        
      print("Vous ne pouvez pas entrer de lettres à caractères spéciaux (sauf les accents) ou plusieurs lettres à la fois !")
    
    else :
        
      fois = mot.count(lettre_entre)
      l_utilises = l_utilises + list(lettre_entre)

      for i in range(len(mot)):

        if lettre_entre==mot[i]:
            
          pu()
          goto(0,0)
          pd()
          l_tirets[i]=lettre_entre
          lettre_vrai+=1
          player = vlc.MediaPlayer("sounds\letter_found.wav")
          player.play()

      winning(lettre_vrai, mot)

      if fois==0:
          
        player = vlc.MediaPlayer("sounds\error.wav")
        player.play()
        erreur+=1
        turtle.width(4)
        bonhomme_3(erreur)
        
    pu()
    goto(0,0)
    pd()
    l_tirets=" ".join(l_tirets)
    turtle.write(l_tirets, align="center", font=("Times", 40, "bold"))
           
speed(100)
mainloop()
