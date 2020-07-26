import os.path
import consolidate

<<<<<<< Updated upstream
def TwoPlatesWelding():
=======
def Welding():
>>>>>>> Stashed changes

    cwd = os.getcwd()
    # All the data from deck.yaml is now in the following deck variable

    deck = consolidate.Deck( cwd + "/TwoPlatesWelding.yaml" )
    
    meshes = consolidate.MeshTwoPlates( deck )
    
    model_HT= consolidate.HeatTransfer(deck,meshes)
    
    model_IC = consolidate.IntimateContact(meshes,deck)
    
    plots = consolidate.PlotsTwoPlates(deck,meshes,meshes.T,meshes.Dic)
    
    solves = consolidate.SolvesTwoPlates( deck,model_HT,meshes,plots,model_IC)

    return {'deck':deck, 'meshes': meshes}

def Printing3D():
        

    deck = directory.Deck( cwd + "/3Dprinting.yaml" )
        
    whatever
    
    return (something)
 
    

if __name__ == '__main__':
<<<<<<< Updated upstream
    print('select Welding or 3Dprinting')
    mode = input()
    if mode == 'Welding':
        result=TwoPlatesWelding()
    elif mode == '3Dprinting':
        Printing3D()

=======
    print('select Welding or Printing3D')
    mode = input()
    if mode == 'Welding':
        result=Welding()
    elif mode == '3Dprinting':
        serginho()
        meshserginho=Printing3D()
>>>>>>> Stashed changes
    else:
       print("Error. Unknown mode")


# result['meshes'].T