from consolidate import *



cwd = os.getcwd()
# All the data from deck.yaml is now in the following deck variable

deck = Deck( cwd + "/deck_printing3D.yaml" )
# deck = Deck( cwd + "/TwoPlates.yaml" )


geometry = Geometry(deck)

meshes = Meshes( deck,geometry )


model_HT= HeatTransfer(deck,meshes)

# model_IC = IntimateContact(meshes,deck)

# plots=PlotsTwoPlates(deck,meshes,meshes.T,meshes.Dic)

# solves = SolvesTwoPlates( deck,model_HT,meshes,plots,model_IC)

