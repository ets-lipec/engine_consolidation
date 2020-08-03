import numpy as np

class Printing_3D:
    
    def __init__(self, deck):
        
        self.deck = deck
        self.do_meshing()
        self.structure_filament(self.meshing)
        
    def do_meshing(self):
        
        self.dimension = self.doc["Problem Type"]["Dimension"]
        
# =============================================================================
# # Number of filaments
#         
#         self.nxfil = self.doc["Dimensions"]["Number of filaments"]["Height"]
#         self.nyfil = self.doc["Dimensions"]["Number of filaments"]["Width"]
#         self.nzfil = self.doc["Dimensions"]["Number of filaments"]["Length"]
#         
# # Number of intervals per filament
#         
#         self.ndx = self.doc["Simulation"]["Number of intervals per filament"]["Thickness"]
#         self.ndy = self.doc["Simulation"]["Number of intervals per filament"]["Width"]
#         self.ndz = self.doc["Simulation"]["Number of intervals per filament"]["Length"]
#         
# # Number of elements
#         
#         self.nxtot = self.nxob*self.ndx+1
#         self.nytot = self.nyob*self.ndy+1
#         self.nztot = self.nzob*self.ndz+1
#         
# =============================================================================
        
        if self.dimension != 1 or 2 or 3:
            
            return ('Wrong dimension')
        
        elif self.dimension >= 1:
            
            self.nxfil = self.doc["Dimensions"]["Number of filaments"]["Height"]
            self.ndx = self.doc["Simulation"]["Number of intervals per filament"]["Thickness"]
            self.nxtot = self.nxfil*self.ndx+1
            self.meshing = np.ones(self.nxtot)
            
        elif self.dimension >= 2:
            
            self.nyfil = self.doc["Dimensions"]["Number of filaments"]["Width"]
            self.ndy = self.doc["Simulation"]["Number of intervals per filament"]["Width"]
            self.nytot = self.nyfil*self.ndy+1
            self.meshing = np.ones((self.nxtot,self.nytot))
            
        elif self.dimension >= 3:
            
            self.nzfil = self.doc["Dimensions"]["Number of filaments"]["Length"]
            self.ndz = self.doc["Simulation"]["Number of intervals per filament"]["Length"]
            self.nztot = self.nzfil*self.ndz+1
            self.meshing = np.ones((self.nxtot,self.nytot,self.nztot))
            
        return (self.meshing)
        
    def structure_filament(self,filament):
        
        if len(filament.shape) == 1:
            
            self.structure1 = filament[1:-1]
            self.structure0 = np.array((filament[0],filament[-1]))
            
        elif len(filament.shape) == 2:
        
            self.structure2 = filament[1:-1,1:-1]
            self.structure1 = np.array((filament[0,1:-1],filament[-1,1:-1],filament[1:-1,0],filament[1:-1,-1]))
            self.structure0 = np.array(())
        
        elif len(filament.shape) == 3:
            
            self.structure3 = filament[1:-1,1:-1,1:-1]
            self.structure2 = np.array((filament[0,1:-1,1:-1],filament[-1,1:-1,1:-1],filament[1:-1,0,1:-1],filament[1:-1,-1,1:-1],filament[1:-1,1:-1,0],filament[1:-1,1:-1,-1]))
            self.structure1 = np.array((filament[0,0,1:-1],filament[0,-1,1:-1],filament[0,1:-1,0],filament[0,1:-1,-1],filament[-1,0,1:-1],filament[-1,-1,1:-1],filament[-1,1:-1,0],filament[-1,1:-1,-1],filament[1:-1,0,0],filament[1:-1,0,-1],filament[1:-1,-1,0],filament[1:-1,-1,-1]))
            self.structure0 = np.array ((filament[0,0,0],filament[0,0,-1],filament[0,-1,0],filament[0,-1,-1],filament[-1,0,0],filament[-1,0,-1],filament[-1,-1,0],filament[-1,-1,-1]))
            
# =============================================================================
#             self.volume = 
#             self.surface = 
#             self.edge = 
#             self.corner = 
# =============================================================================

    # def filament_deposition(self,U,x,y,z):
        
    #     U[]