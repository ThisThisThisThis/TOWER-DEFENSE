from tkinter import *
import time
import threading


########################################################## Classes #####################################################################
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
                        print(self.structure)
        def afficher(self, fenetre):
                """Méthode permettant d'afficher le niveau en fonction 
                de la liste de structure renvoyée par generer()"""
                self.fond= PhotoImage(file="images/fond.gif")
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
                                        
                                
                                        
                                num_case += 1
                        num_ligne += 1
                


class Mechant:
        def __init__(self,niveau,vitesse):
                self.case_x=0
                self.case_y=0
                self.x = 0
                self.y = 0
                self.niveau= niveau
                self.vitesse=vitesse
        def creation(self):
                self.monstre=PhotoImage(file="images/monstre.gif")
                self.img_monstre=canvas.create_image(self.case_x,self.case_y,image=self.monstre,anchor=NW)
               
        def deplacement(self):
                if self.case_y < 13:
                        if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                                self.case_y += 1
                                self.y = self.case_y * taille_sprite
                                canvas.coords(self.img_monstre,self.x,self.y)
                                canvas.after(self.vitesse,self.deplacement)
                                
                
                if self.case_x < 28:
                        if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                                self.case_x += 1
                                self.x = self.case_x * taille_sprite
                                canvas.coords(self.img_monstre,self.x,self.y)
                                canvas.after(self.vitesse,self.deplacement)

                if self.case_x < 28:               
                        if self.niveau.structure[self.case_y][self.case_x+1] == 'a':
                                canvas.delete(self.img_monstre)
                                
                               
                                
   

                        

###################################################################################################################


fenetre=Tk()


canvas = Canvas(fenetre, width=1500, height=950)
canvas.pack()
choix = 'niveaux1'
taille_sprite=50
niveau = Niveau(choix)
niveau.generer()
niveau.afficher(fenetre)



def lancer():
        mechant=Mechant(niveau,500)
        mechant.creation()
        mechant.deplacement()
        
Button(fenetre,text="LANCER",command=lancer,anchor=S).pack()       




fenetre.mainloop()    
