from tkinter import *
from constantes import *


class Niveau:
        """Classe permettant de créer un niveau"""
        def __init__(self,fichier):
                self.structure = 0
                self.fichier = fichier
        
        def generer(self):
                

                """Méthode permettant de générer le niveau en fonction du fichier.
                On crée une liste générale, contenant une liste par ligne à afficher""" 
                #On ouvre le fichier
                with open(self.fichier, "r") as fichier:
                        structure_niveau = []
                        #On parcourt les lignes du fichier
                        for ligne in fichier:
                                ligne_niveau = []
                                #On parcourt les sprites (lettres) contenus dans le fichier
                                for sprite in ligne:
                                        #On ignore les "\n" de fin de ligne
                                        if sprite != '\n':
                                                #On ajoute le sprite à la liste de la ligne
                                                ligne_niveau.append(sprite)
                                #On ajoute la ligne à la liste du niveau
                                structure_niveau.append(ligne_niveau)
                        #On sauvegarde cette structure
                        self.structure = structure_niveau
                        
        
        def afficher(self, fenetre):
                """Méthode permettant d'afficher le niveau en fonction 
                de la liste de structure renvoyée par generer()"""
                self.fond= PhotoImage(file="images/fond.gif")
                canvas = Canvas(fenetre, width=1500, height=950)
                canvas.create_image(0,0, anchor = NW, image=self.fond)

                self.mur = PhotoImage(file="images/mur.gif")
                self.depart = PhotoImage(file="images/depart.gif")
                self.arrivee = PhotoImage(file="images/arrivee.gif")
                self.trol = PhotoImage(file="images/trol.gif")
                
                #On parcourt la liste du niveau
                num_ligne = 0
                for ligne in self.structure:
                        #On parcourt les listes de lignes
                        num_case = 0
                        for sprite in ligne:
                                #On calcule la position réelle en pixels
                                x = num_case * taille_sprite
                                y = num_ligne * taille_sprite
                                if sprite == 'm':                  #m = Mur
                                       canvas.create_image(x, y,anchor = NW,image=self.mur)
                                elif sprite == 'd':                #d = Départ
                                        canvas.create_image(x, y,anchor = NW,image=self.depart)
                                        
                                elif sprite == 'a':               #a = Arrivée
                                        canvas.create_image(x, y,anchor = NW,image=self.arrivee)
                                        
                                elif sprite == 'b':
                                        canvas.create_image(x, y,anchor = NW,image=self.trol)
                                        
                                num_case += 1
                        num_ligne += 1
                canvas.pack()


class Mechant:
    def __init__(self):
        self.case_x=0
        self.case_y=0
        self.x = 0
        self.y = 0
        



    def creation(self):
        img=PhotoImage(file='images/test.gif')
        self.img=canvas.create_(sel.x,self.y,image=img)

        
   ####def deplacement(self):
       # while self.niveau.structure[self.case_y][self.case_x+1] !='m':
          #  self.case_x += 1
            #Calcul de la position "réelle" en pixel
           # self.x = self.case_x * taille_sprite
                        

