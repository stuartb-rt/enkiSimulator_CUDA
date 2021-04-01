
import numpy as np
import matplotlib.pylab as plt


path = "./"
spath = "./"

sizeY=3
ratioYX=4
my_dpi=300
plt.close("all")

 #%%

wchraw=np.loadtxt('weight_distances.tsv')
nLayers=wchraw.shape[1]
plt.figure('weigth change')
plt.plot(wchraw[:,3], color = "black", linewidth=0.3 )
plt.show()