
class MT:
    def __init__(self, état_initial, état_final, position, programme, ruban):
        self.état = état_initial
        self.état_final = état_final
        self.position = position
        self.ruban = ruban
        self.programme = programme # dictionnaire {(etat , caractere_lu) : (etat-a-prendre , caractere-a-ecrire , mouvement-a-faire(d, g ,n))  == TRANSITION} 

    def pas_de_calcul(self):
        position = self.position
        assert position < len(self.ruban), "La position {position} dépasse la longueur de la liste" # la postion doit etre inferieur a la longeur du ruban ,assert le verifie , donc si la condition ,'est pas verifier asserte bloque le programme
        assert position >=0, "La position {position} est négative" # si assert n'est pas verifier (>0) alors la position est <0
        état=self.état # 001101
        caractère_lu=self.ruban[position] #0
        self.ruban[position]=self.programme[(état,caractère_lu)][1] # 1 0 D , modifier le caractere a ecrire  
        if self.programme[(état,caractère_lu)][2]=='D':  # je lis le mouvement a faire et j'avance en fonction du mouvement 
            self.position = position +1
        elif self.programme[(état,caractère_lu)][2]=='G':
            self.position = position -1 
        self.état= self.programme[(état,caractère_lu)][0] #0  definir le nouveau etat a prendre 


    def exécution(self):
        print(f"Ruban avant : {self.ruban}")
        while self.état != self.état_final:
            m.pas_de_calcul()
        print(f"Etat final de la machine : {m}") 
        print(f"Ruban après : {self.ruban}")

    def __str__(self):
        return f"Etat : {self.état}, position : {self.position}, caractère lu :{self.ruban[self.position]}"
    

objectif="complémenter un liste de 0 et de 1"
programme = {("début","0"):("début", "1", "D"),("début","1"):("début", "0", "D"),("début"," "):("fin"," ", "N") } # ma liste de transitions 
ruban = ["1","0","0","0","1","0","0","0","0","1","0","0"," "]
état_initial="début"
état_final="fin"
print(f"Objectif : {objectif}")
m=MT(état_initial, état_final, 0, programme, ruban) 
m.exécution()

objectif="La liste a-t-elle un nombre pair de zéros ?"
programme = {("pair","0"):("impair", "0", "D"),
             ("pair","1"):("pair", "1", "D"),
             ("impair","0"):("pair", "0", "D"),
             ("impair","1"):("impair", "1", "D"),
             ("pair"," "):("final", "nbre pair de zéros", "N"),
             ("impair"," "):("final", "nbre impair de zéros", "N")}
ruban = ["0","0","0","0","1","0","0","0","0","1","0","0","0","0","1"," "]
état_initial="pair"
état_final="final"
print(f"Objectif : {objectif}")
m=MT(état_initial, état_final, 0, programme, ruban)
  
m.exécution()

objectif = "Additionner deux nombres"
programme = {("q1","1"):("q2", "0", "D"), # départ on efface le 1 le plus à gauche
             ("q2","1"):("q2", "1", "D"), # on se déplace à droite tant qu'on a des 1
             ("q2","0"):("q3", "1", "G"), # on remplace par 1 on se déplace à gauche
             ("q3","1"):("q3", "1", "G"), # on recule tant qu'on a des 1
             ("q3","0"):("q4", "0", "D"),
             ("q4","1"):("qf", "0", "D"),
            }
ruban = ["1","1","1","1","0","1","1","1","1","1","0","0","0"," "]
état_initial="q1"
état_final="qf"
position_initiale = 0
print(f"Objectif : {objectif}")
m=MT(état_initial, état_final, position_initiale, programme, ruban)
m.exécution()



######################################################
#                    2 éme partie                    #             
#                                                    #
######################################################


class RUBAN: #bi-infini

    def __init__(self, caracteres="", blanc=" "):
        self.caractere = caracteres
        self.blanc = blanc
        

    def gauche(self): 
        #Décale la tête du ruban vers la gauche
        self.position = self.position -1

    def droite(self):
        #Décale la tête du ruban vers la droite.
        self.position = self.position +1
    
    def ecrit(self, caractère):
        #Écrit un caractere à l’emplacement courant de la tête de lecture.
        if self.tete < len(self.caractere) :
            self.caractere[self.tete] = caractère
        else:
            self.caractere.append(caractère)
    
    
    def lit(self):
       # Retourne le caractère courant.
        if self.tete < len(self.caractere):
            return self.caractere[self.tete]
        else:
            return self.blanc
      
    def __str__(self):
        return str(self.caractere[:self.tete] +  str(self.caractere[self.tete:]))

class MTBIFINI:
    def __init__(self, état_initial, état_final, programme, Ruban):
         self.état = état_initial
         self.état_final = état_final
         self.Ruban = RUBAN(Ruban) 
         self.programme = programme # TRANSITION
       
    def pas_de_calcul(self):

        état=self.état # 001101
        caractère_lu = self.Ruban.lit() #0
        self.Ruban.ecrit()# 1 0 D , modifier le caractere a ecrire  
        if self.Ruban.lit() == 'D':  # je lis le mouvement a faire et j'avance en fonction du mouvement 
            self.Ruban.droite()
        elif self.Ruban.lit() == 'G' :
            self.Ruban.gauche() 
        self.état= self.programme[(état,caractère_lu)][0] #0  definir le nouveau etat a prendre 
    
    def exécution(self):
        print(f"Ruban avant : {self.Ruban}") #f c juste pour m'afficher ce quil ya dans les {}  comme + ...
        while self.état != self.état_final:
            m.pas_de_calcul()
        print(f"Etat final de la machine : {m}")
        print(f"Ruban après : {self.Ruban}")
 
           
class RUBANIND(RUBAN): #infini a droite
    def __init__(self):
        super().__init__()
    
    def droite(self):
        
        super().droite()
    
    def ecrit(self, caractère):
        super().ecrit()
    
    def lit(self):
        super().lit()
        
    def __str__(self):
        super().__str__()


class MTD(MTBIFINI):
    def __init__(self, état_initial, état_final, programme, Ruban):
        super().__init__(état_initial, état_final, programme, Ruban)
   
    def pas_de_calcul(self):

        état=self.état 
        caractère_lu = self.Ruban.lit()
        self.Ruban.ecrit()  
        if self.Ruban.lit() == 'D':   
            self.Ruban.droite()
        self.état= self.programme[(état,caractère_lu)][0]
    def exécution(self):
        return super().exécution()

 
def equivalente(MTB):
    #machine de turing avec ruban bifini
   
    mtd = MTD #machine de turing avec ruban infini a droite
    mtd.__init__ = MTB.__init__
    mtd.pas_de_calcul = MTB.pas_de_calcul
    mtd.exécution = MTB.exécution
    return mtd

"""
objectif="La liste a-t-elle un nombre pair de zéros ?"
programme = {("pair","0"):("impair", "0", "D"),
             ("pair","1"):("pair", "1", "D"),
             ("impair","0"):("pair", "0", "D"),
             ("impair","1"):("impair", "1", "D"),
             ("pair"," "):("final", "nbre pair de zéros", "N"),
             ("impair"," "):("final", "nbre impair de zéros", "N")}
ruban = ["0","0","0","0","1","0","0","0","0","1","0","0","0","0","1"," "]
état_initial="pair"
état_final="final"
m=MT(état_initial, état_final,0, programme, ruban)
d=equivalente(m)
"""

class MTC(MT):
    def __init__(self, état_initial, état_final, position, programme, ruban , alphabet):
        super().__init__(état_initial, état_final, position, programme, ruban)
        self.alphabet = alphabet # tuple("a", "b" ,"c" ,"d")
    def pas_de_calcul(self):
        return super().pas_de_calcul()
    def exécution(self):
        return super().exécution()


def transformation(MTc):
      MTc = MTC(MTc)
      état_initial= MTc.état
      état_final= MTc.état_final 
      position = MTc.position  
      ruban = MTc.ruban
      programme = MTc.programme
      while MTc.état != MTc.état_final:
       if MTc.alphabet == "a":
          ruban[position] = "00"
       elif MTc.alphabet == "b" :
          ruban[position] = "01"
       elif MTc.alphabet == "c" : 
          ruban[position] = "10"
       elif MTc.alphabet == "d" :
          ruban[position] = "11"
                                 
      return  MT(état_initial, état_final, position, programme, ruban) 





