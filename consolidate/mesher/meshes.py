# -*- coding: utf-8 -*-
import numpy as np

class Meshes():

    def __init__(self, deck,geometry):
        self.deck = deck
        self.geometry=geometry
        self.final_meshing()
        
        
        
    def set_mesh_grid(self):
        self.nx = int(self.deck.doc["Simulation"]["Number of Elements X"])
        self.ny1 = int(self.deck.doc["Simulation"]["Number of Elements Y1"])
        self.ny2=int(self.deck.doc["Simulation"]["Number of Elements Y2"])
        self.ny=self.ny1+self.ny2+1
    
        self.dx=self.geometry.Lx/self.nx
        self.dy1=self.geometry.Ly1/self.ny1
        self.dy2=self.geometry.Ly2/self.ny2
        self.dhe=self.geometry.Lhe
        
        
        X,Y = np.meshgrid(np.arange(0, self.ny), np.arange(0, self.nx))
        ElementsThickness=X[1,:].copy()
        ElementsWidth=Y[:,1].copy()
        self.ElementsThickness = ElementsThickness.copy()
        self.ElementsWidth = ElementsWidth.copy()
    
        
        
        
    def set_dx(self):
        Mdx=np.zeros((self.ny, self.nx)) 
        Mdx[0:self.ny, 0:self.nx]=self.dx
        self.Mdx=Mdx.copy()
    
    def set_dy(self):
        Mdy=np.zeros((self.ny, self.nx)) 
        Mdy[0:self.ny1, 0:self.nx]=self.dy1
        Mdy[self.ny1:self.ny, 0:self.nx]=self.dy2
        Mdy[self.ny1, 1:-1]=self.dhe
        self.Mdy=Mdy.copy()
        z
    def set_temperatures(self):
        T = np.zeros((self.ny, self.nx))        
        T[0:self.ny1, 0:self.nx] = self.deck.doc["Materials"]["Material1"]["Initial Temperature"] # Set array size and set the interior value with Tini
        T[self.ny1:self.ny, 0:self.nx] = self.deck.doc["Materials"]["Material2"]["Initial Temperature"] # Set array size and set the interior value with Tini
        T[self.ny1, 1:-1] = self.deck.doc["Processing Parameters"]["Temperature"]

        self.T = T.copy()
        self.T0=T.copy()
        
      
    def set_conductivity(self):
        KtotalX= np.zeros((self.ny, self.nx)) 
        KtotalX[0:self.ny1, 0:self.nx] = self.deck.doc["Materials"]["Material1"]["Thermal Conductivity X"]
        KtotalX[self.ny1:self.ny, 0:self.nx] = self.deck.doc["Materials"]["Material2"]["Thermal Conductivity X"]
        KtotalX[self.ny1, 1:-1]=3.0
        self.KtotalX=KtotalX
                                                                                         
        KtotalY= np.zeros((self.ny, self.nx)) 
        KtotalY[0:self.ny1, 0:self.nx] = self.deck.doc["Materials"]["Material1"]["Thermal Conductivity Y"]
        KtotalY[self.ny1:self.ny, 0:self.nx] = self.deck.doc["Materials"]["Material2"]["Thermal Conductivity Y"]      
        KtotalY[self.ny1, 1:-1]=3.0                                                                             
        self.KtotalY=KtotalY         

    def set_density(self):
        RhoTotal= np.zeros((self.ny, self.nx)) 
        RhoTotal[0:self.ny1, 0:self.nx] = self.deck.doc["Materials"]["Material1"]["Density"]
        RhoTotal[self.ny1:self.ny, 0:self.nx] = self.deck.doc["Materials"]["Material2"]["Density"]    
        RhoTotal[self.ny1, 1:-1]=4600                                                                            
        self.RhoTotal=RhoTotal  

    def set_specific_heat(self):
        CpTotal= np.zeros((self.ny, self.nx)) 
        CpTotal[0:self.ny1, 0:self.nx] = self.deck.doc["Materials"]["Material1"]["Cp"]
        CpTotal[self.ny1:self.ny, 0:self.nx] = self.deck.doc["Materials"]["Material2"]["Cp"]     
        CpTotal[self.ny1, 1:-1]=700                                                                              
        self.CpTotal=CpTotal  

    def set_diffusivity(self):                                                                                  
        DiffTotalX = np.zeros((self.ny, self.nx)) 
        DiffTotalX[0:,0:]=self.KtotalX[0:,0:]/(self.RhoTotal[0:,0:]*self.CpTotal[0:,0:])
        self.DiffTotalX = DiffTotalX.copy()
        
        DiffTotalY = np.zeros((self.ny, self.nx)) 
        DiffTotalY[0:,0:]=self.KtotalY[0:,0:]/(self.RhoTotal[0:,0:]*self.CpTotal[0:,0:])
        self.DiffTotalY = DiffTotalY.copy()

    def set_viscosity(self):         
        Visc=np.zeros((self.ny, self.nx))
        Visc[0:, 0:]=1.14*10**(-12)*np.exp(26300/self.T[0:, 0:])
        self.Visc=Visc.copy()

    def set_dic(self):
        Dic=np.ones((self.ny, self.nx))
        self.dic=1/(1+0.45)
        Dic[self.ny1,1:-1]=self.dic
        self.Dic0=Dic.copy()
        self.Dic=Dic.copy()   


    def set_heat_density(self):       
        self.q=float(self.deck.doc["Processing Parameters"]["Power Density"])
        Q=np.zeros((self.ny, self.nx))
        Q[int(self.ny/2), 0:] = self.q
        Q[int(self.ny/2-1), 0:] = self.q
        self.Q=Q.copy()


    def dist(self):
        
        self.distThickness=np.zeros((self.ny))
        self.distThickness[0:self.ny1+1]=self.ElementsThickness[0:self.ny1+1]*self.dy1
        self.distThickness[self.ny1+1]=self.distThickness[self.ny1]+self.dhe
        self.distThickness[self.ny1+2:self.ny]=self.distThickness[self.ny1+1]+self.ElementsThickness[1:self.ny2]*self.dy2
        # DistY[self.ny1, 1:-1]=self.dhe
      
        
        
# ----------------------------------------------------


    def do_meshing(self):
            
           
    # =============================================================================
    # # Number of filaments
    #         
    #         self.nxfil = self.deck.doc["Dimensions"]["Number of filaments"]["Height"]
    #         self.nyfil = self.deck.doc["Dimensions"]["Number of filaments"]["Width"]
    #         self.nzfil = self.deck.doc["Dimensions"]["Number of filaments"]["Length"]
    #         
    # # Number of intervals per filament
    #         
    #         self.ndx = self.deck.doc["Simulation"]["Number of intervals per filament"]["Thickness"]
    #         self.ndy = self.deck.doc["Simulation"]["Number of intervals per filament"]["Width"]
    #         self.ndz = self.deck.doc["Simulation"]["Number of intervals per filament"]["Length"]
    #         
    # # Number of elements
    #         
    #         self.nxtot = self.nxob*self.ndx+1
    #         self.nytot = self.nyob*self.ndy+1
    #         self.nztot = self.nzob*self.ndz+1
    #         
    # =============================================================================
    
            
            self.nxfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Height"])
            self.ndx = int(self.deck.doc["Simulation"]["Number of intervals per filament"]["Thickness"])
            self.nxtot = self.nxfil*self.ndx+1
            self.meshing = np.ones(self.nxtot)
            self.x = np.linspace(0,self.geometry.lenXtot,self.nxtot)
                
            if self.deck.dimension >= 2:
                
                self.nyfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Width"])
                self.ndy = int(self.deck.doc["Simulation"]["Number of intervals per filament"]["Width"])
                self.nytot = self.nyfil*self.ndy+1
                self.meshing = np.ones((self.nxtot,self.nytot))
                self.y = np.linspace(0,self.geometry.lenYtot,self.nytot)
                self.Y,self.X = np.meshgrid(self.y,self.x)
                
            elif self.deck.dimension >= 3:
                
                self.nzfil = int(self.deck.doc["Dimensions"]["Number of filaments"]["Length"])
                self.ndz = int(self.deck.doc["Simulation"]["Number of intervals per filament"]["Length"])
                self.nztot = self.nzfil*self.ndz+1
                self.meshing = np.ones((self.nxtot,self.nytot,self.nztot))
                self.z = np.linspace(0,self.geometry.lenZtot,self.nztot)
                self.Y,self.X,self.Z = np.meshgrid(self.y,self.x,self.z)
    
                        
       
        
        
        
        
        
  # ---------------------------------------------------      
        
    def final_meshing(self):

        if self.deck.doc["Problem Type"]["Name"] == "TwoPlates":
            self.set_mesh_grid() 
            self.set_dx()
            self.set_dy()
            self.set_temperatures()
            self.set_conductivity()
            self.set_density()
            self.set_specific_heat()
            self.set_diffusivity()
            self.set_viscosity()   
            self.set_dic()
            self.set_heat_density()
            self.dist()
            
            
        elif self.deck.doc["Problem Type"]["Name"] == "Printing3D":
            self.do_meshing()
            
       
        