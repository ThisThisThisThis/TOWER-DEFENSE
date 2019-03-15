
from tkinter import *
import time




########################################################## Classes #####################################################################


class Niveau:
        """Classe permettant de créer un niveau"""
        def __init__(self,fichier):
                self.liste = 0
                self.fichier = fichier
        
        def generer(self):
                """Méthode permettant de générer le niveau en fonction du fichier.
                On crée une liste générale, contenant une liste par ligne à afficher""" 
                #On ouvre le fichier
                with open(self.fichier, "r") as fichier:
                        structure_niveau = []
                        #On parcourt les lignes du filter                                                                                       
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
                        self.liste = structure_niveau
                        
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
                for ligne in self.liste:
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
                self.niveau=niveau
                self.vitesse=vitesse
                self.vie=20
                self.monstre=PhotoImage(file="images/monstre.gif")
                self.img_monstre=canvas.create_image(self.case_x,self.case_y,image=self.monstre,anchor=NW)
               

        def deplacement(self):
                droite=0
                bas=0
                if self.case_x < 24:
                        if niveau.liste[self.case_y][self.case_x+1] == 'a':           
                                canvas.delete(self.img_monstre)
                if self.case_y < 10:
                        if niveau.liste[self.case_y+1][self.case_x] != 'm':
                                bas=1
                if self.case_x < 24:
                        if niveau.liste[self.case_y][self.case_x+1] != 'm':
                                droite=1

                if bas==1:
                        self.case_y += 1
                        self.y = self.case_y * taille_sprite
                        canvas.coords(self.img_monstre,self.x,self.y)
                        canvas.after(self.vitesse,self.deplacement)
                if droite==1:
                        self.vie-=1
                        self.case_x += 1
                        self.x = self.case_x * taille_sprite
                        canvas.coords(self.img_monstre,self.x,self.y)
                        canvas.after(self.vitesse,self.deplacement)

class Tour:
        def __init__(self,niveau,xdepart,ydepart):
                self.xdepart=xdepart
                self.ydepart=ydepart
                self.niveau=niveau
                self.tour_image1= PhotoImage(file="images/tour1.gif")
                self.cercleVT1_image=PhotoImage(file="images/cercle_vertT1.gif")
                self.cercleRT1_image=PhotoImage(file="images/cercle_rougeT1.gif")

                self.tour1_menu=canvas.create_image(xdepart,ydepart,anchor=NW,image=self.tour_image1)
                

        def clic(self,event):
                """ Gestion de l'événement Clic gauche """
                global DETECTION_CLIC_SUR_OBJET

                # position du pointeur de la souris
                X = event.x
                Y = event.y
                # coordonnées de l'objet
                [xmin,ymin,xmax,ymax] = canvas.bbox(self.tour1_menu)
                
                if xmin<=X<=xmax and ymin<=Y<=ymax:
                        DETECTION_CLIC_SUR_OBJET = True
                        
                        self.cercle_vertT1=canvas.create_image(self.xdepart-90,self.ydepart-60,anchor=NW,image=self.cercleVT1_image)
                        self.tour1=canvas.create_image(self.xdepart,self.ydepart,anchor=NW,image=self.tour_image1)

                        
                        [self.xminT,self.yminT,self.xmaxT,self.ymaxT]= canvas.bbox(self.tour1)

                else:
                        DETECTION_CLIC_SUR_OBJET = False

                

        def drag(self,event):
                """ Gestion de l'événement bouton gauche enfoncé """
                X = event.x
                Y = event.y
                
                if DETECTION_CLIC_SUR_OBJET == True:
                        # limite de l'objet dans la zone graphique
                        if X<0:X=0
                        if X>largeur: X=largeur-(self.xmaxT-self.xdepart)
                        if Y<0: Y=0
                        if Y>hauteur: Y=hauteur-(self.ymaxT-self.ydepart)
                        # mise à jour de la position de l'objet (drag)
                        canvas.coords(self.tour1,X-28,Y-40)
                        canvas.coords(self.cercle_vertT1,X-118,Y-100)
                        canvas
                        [self.xminTF,self.yminTF,self.xmaxTF,self.ymaxTF]= canvas.bbox(self.tour1)

                               



        def test(self,event):
                if  self.yminTF>(12*taille_sprite-81):
                       canvas.delete(self.tour1) 
                       canvas.delete(self.cercle_vertT1)
                else:
                        canvas.delete(self.cercle_vertT1)
                


###################################################################################################################


fenetre=Tk()
largeur=1500
hauteur=950

canvas = Canvas(fenetre, width=largeur, height=hauteur)
canvas.pack()
choix = 'niveaux1'
taille_sprite=60

niveau = Niveau(choix)
niveau.generer()
niveau.afficher(fenetre)

tour= Tour(niveau,100,750)
DETECTION_CLIC_SUR_OBJET = False



canvas.bind('<Button-1>',tour.clic) # évévement clic gauche (press)
canvas.bind('<B1-Motion>',tour.drag) # événement bouton gauche enfoncé (hold down)
canvas.bind('<ButtonRelease-1>',tour.test)

def lancer():
        mechant=Mechant(niveau,400)
        mechant.deplacement()
        
Button(fenetre,text="LANCER",command=lancer,anchor=S).pack()       




fenetre.mainloop()    

