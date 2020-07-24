

class HeatTransfer:

    def do_timestep(self, T):
        
        if len(T.shape) == 1:
            
            T[1:-1] = T[1:-1] + self.Dx * self.dt * ((T[2:] - 2*T[1:-1] + T[:-2]) / self.dx**2)
            
        elif len(T.shape) == 2:
            
            T[1:-1, 1:-1] = T[1:-1, 1:-1] + self.Dx * self.dt * ((T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1]) / self.dx**2) + self.Dy * self.dt * ((T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2]) / self.dy**2)
            
        elif len(T.shape) == 3:
            
            T[1:-1, 1:-1, 1:-1] = T[1:-1, 1:-1, 1:-1] + self.Dx * self.dt * ((T[2:, 1:-1, 1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[:-2, 1:-1, 1:-1]) / self.dx**2) + self.Dy * self.dt * ((T[1:-1, 2:, 1:-1] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, :-2, 1:-1]) / self.dy**2) + self.Dz * self.dt * ((T[1:-1, 1:-1, 2:] - 2*T[1:-1, 1:-1, 1:-1] + T[1:-1, 1:-1, :-2]) / self.dz**2) 
            
        else:
            
            return ('Wrong dimension')
        
        return T