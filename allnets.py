import numpy as np

def flipmatrix(net):        # Turns a net upside-down
    newmatrix = []
    for row in range( len(net) ):
        newmatrix.append( list(net[( abs(row - len(net) + 1 ) )]) )
    return np.array(newmatrix)

# All basic nets
net1 = np.array([ [0,1,0],[1,1,1],[0,1,0],[0,1,0] ])
net2 = np.array([ [1,1,1],[0,1,0],[0,1,0],[0,1,0] ])
net3 = np.array([ [1,1,0],[0,1,0],[0,1,1],[0,0,1] ])
net4 = np.array([ [1,1,0],[0,1,0],[0,1,1],[0,1,0] ])
net5 = np.array([ [0,1,0],[1,1,0],[0,1,1],[0,1,0] ])
net6 = np.array([ [0,1,1],[0,1,0],[0,1,0],[1,1,0] ])
net7 = np.array([ [0,1,1],[1,1,0],[0,1,0],[0,1,0] ])
net8 = np.array([ [0,0,1],[0,1,1],[1,1,0],[1,0,0] ])
net9 = np.array([ [0,1,0],[0,1,1],[1,1,0],[1,0,0]  ])
net10 = np.array([ [0,1,0],[0,1,0],[1,1,1],[1,0,0] ])
net11 = np.array([ [0,1],[0,1],[1,1],[1,0],[1,0] ])


all_nets = [ net1 , net1.transpose() , flipmatrix(net1) , flipmatrix(net1).transpose(),
            net2 , net2.transpose() , flipmatrix(net2) , flipmatrix(net2).transpose(),
            net3 , net3.transpose() , flipmatrix(net3) , flipmatrix(net3).transpose(),
            net4 , net4.transpose() , flipmatrix(net4) , flipmatrix(net4).transpose(),
            net5 , net5.transpose() , flipmatrix(net5) , flipmatrix(net5).transpose(),
            net6 , net6.transpose() , flipmatrix(net6) , flipmatrix(net6).transpose(),
            net7 , net7.transpose() , flipmatrix(net7) , flipmatrix(net7).transpose(),
            net8 , net8.transpose() , flipmatrix(net8) , flipmatrix(net8).transpose(),
            net9 , net9.transpose() , flipmatrix(net9) , flipmatrix(net9).transpose(),
            net10 , net10.transpose() , flipmatrix(net10) , flipmatrix(net10).transpose(),
            net11 , net11.transpose() , flipmatrix(net11) , flipmatrix(net11).transpose() ]

