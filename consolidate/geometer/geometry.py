# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:38:36 2020

@author: andre
"""


class Geometry():
    def __init__(self, deck):
        self.deck = deck
              
        
        self.final_geometry()
        
    
        
        
    def geometry_welding(self):
        self.Lx=float(self.deck.doc["Geometry"]["Length X"])
        self.Ly1=float(self.deck.doc["Geometry"]["Length Y1"])
        self.Ly2=float(self.deck.doc["Geometry"]["Length Y2"])
        self.Lhe=float(self.deck.doc["Geometry"]["HE"])
        
    
    def geometry_printing(self):
        
        self.dimension = int(self.deck.doc["Problem Type"]["Dimension"])

        if self.dimension not in {1, 2, 3}:

            print ('Wrong dimension')
            sys.exit()

        self.lenXfil = float(self.deck.doc["Dimensions"]["Filament"]["Thickness [m]"])
        self.nxfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Height"])
        self.lenXtot = self.lenXfil * self.nxfil
            
        if self.dimension >= 2:            
            self.lenYfil = float(self.deck.doc["Dimensions"]["Filament"]["Width [m]"])
            self.nyfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Width"])
            self.lenYtot = self.lenYfil * self.nyfil
            
        elif self.dimension >= 3:            
            self.lenZfil = float(self.deck.doc["Dimensions"]["Filament"]["Length [m]"])
            self.nzfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Length"])
            self.lenZtot = self.lenZfil * self.nzfil
         
            
            
      
        
        
    def final_geometry(self):
        if self.deck.doc["Problem Type"]["Name"] == "TwoPlates":
            self.geometry_welding()
            
            
        elif self.deck.doc["Problem Type"]["Name"] == "Printing3D":
            self.geometry_printing()
           