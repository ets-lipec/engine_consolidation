import numpy as np

class HeatTransfer:

    def __init__(self, deck,meshes):
        self.dt = float(deck.doc["Simulation"]["Time Step"])
        self.dx2 = meshes.Mdx*meshes.Mdx
        self.dy2 = meshes.Mdy*meshes.Mdy
        self.rho=meshes.RhoTotal
        self.cp=meshes.CpTotal
        self.k=meshes.KtotalX
        
# -------------- BEGIN HEAT TRANSFER CALCULATION---------- 
    def do_timestep_welding(self, u0, u, Diffx, Diffy,Q):
        # Propagate with forward-difference in time, central-difference in space
        u[1:-1, 1:-1] = u0[1:-1, 1:-1] + Diffy[1:-1, 1:-1]* self.dt * ((u0[2:, 1:-1] - 2*u0[1:-1, 1:-1] + u0[:-2, 1:-1])/self.dy2[1:-1, 1:-1] ) + Diffx[1:-1, 1:-1]* self.dt * ( (u0[1:-1, 2:] - 2*u0[1:-1, 1:-1] + u0[1:-1, :-2])/self.dx2[1:-1, 1:-1] ) + self.dt*Q[1:-1,1:-1]/(self.cp[1:-1,1:-1]*self.rho[1:-1,1:-1])

        u0 = u.copy()
        
        return u0, u
 # -------------- END HEAT TRANSFER CALCULATION---------- 
        
    # def convection(self, h, k, T, Tout, sign):

    #     # sign = 1 if position (T) > position (Tout)
    #     # sign = -1 if position (T) < position (Tout)
    #     # h = convective coeffiecient
    #     # k = thermal conductivity
    #     # T= current temperature
    #     # Tout=room temperature
        
    #     return (signh(T-Tout)/k)   
    
    
    
# ----------------------------------------    
    
    
    def do_timestep_printing(self, T, Dx, Dy=None, Dz=None, Q=np.zeros((1,1,1))):
    
        if len(T.shape) == 1:
            
            T[1:-1] = T0[1:-1] + Dx * self.dt * ((T[2:] - 2*T[1:-1] + T[:-2]) / self.dx**2) + Q[1:-1] * self.dt / (self.rho*self.Cp)
            
        elif len(T.shape) == 2:
            
            T[1:-1, 1:-1] = T[1:-1, 1:-1] + Dx * self.dt * ((T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1]) / self.dx**2) + Dy * self.dt * ((T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2]) / self.dy**2) + Q[1:-1,1:-1] * self.dt / (self.rho*self.Cp)
            
        elif len(T.shape) == 3:
            
            T[1:-1, 1:-1, 1:-1] = T[1:-1, 1:-1, 1:-1] + Dx * self.dt * ((T[2:, 1:-1, 1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[:-2, 1:-1, 1:-1]) / self.dx**2) + Dy * self.dt * ((T[1:-1, 2:, 1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, :-2, 1:-1]) / self.dy**2) + Dz * self.dt * ((T[1:-1, 1:-1, 2:] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, 1:-1, :-2]) / self.dz**2) + Q[1:-1,1:-1,1:-1] * self.dt / (self.rho*self.Cp) 
            
        else:
            
            return ('Wrong dimension')
    
        return T

    def convection_printing(self, h, k, T, Tout, sign):
        
        # sign = 1 if position (T) > position (Tout)
        # sign = -1 if position (T) < position (Tout)
        
        return (sign*h*(T-Tout)/k)
    
    
    
    def final_do_timestep(self):
            if self.deck.doc["Problem Type"]["Name"] == "TwoPlates":
                self.do_timestep_welding()
                
                
            elif self.deck.doc["Problem Type"]["Name"] == "Printing3D":
                self.do_timestep_printing()
                self.convection_printing()
               
    
