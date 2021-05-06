# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 18:13:03 2018

@author: sama
"""

import numpy as np
import matplotlib.pylab as plt
import bpPlotClass as bpc
import matplotlib.image as mpimg

plt.rcParams['font.family'] = 'serif'
plt.rcParams.update({'font.size': 9})

path='/home/sama/enkiSimulator_CUDA/examples/line_follower/'
spath='./'
#sizeY=3
#ratioYX=4
#my_dpi=300

plt.close("all")


#%%
error=np.loadtxt('{}errorData.tsv'.format(path));
#minE=min(error); maxE=max(abs(error))
errorNorm=error #/maxE
errorfig=plt.figure('error')
axe=errorfig.add_subplot(111)
plt.plot(error, color='black', linestyle="-", linewidth=0.5)
plt.xlabel("Step Count")
plt.ylabel("Closed-Loop Error")
#plt.ylim(-0.3, 0.3)
#plt.yticks([-0.2, -0.1, 0, 0.1, 0.2])
#plt.xticks(np.arange(0,len(error),250))
#axe.set_aspect(aspect=len(error)/(.6*3))
errorfig.savefig(spath+'error_signal', quality= 100, format='svg', bbox_inches='tight')
plt.show()

#%%

coofig=plt.figure('coordinates')
coorddata=np.loadtxt('{}coordData.tsv'.format(path));
img=mpimg.imread('{}cc.png'.format(path))
imgplot = plt.imshow(img)
plt.plot((coorddata[:,0])*4, 1000-(coorddata[:,1])*4, color='black', linestyle="--", linewidth=0.5)
#plt.scatter(4*[0,160,0,160], 4*[0,0,200,200], color='black')
coofig.savefig(spath+'coordData', quality=100, format='svg', bbox_inches='tight')
plt.show()

#%%

statRaw=np.loadtxt('{}stats.tsv'.format(path))
stat=statRaw.astype(np.int16)
numPredictors=stat[0]
numLayerNeurons=stat[1::]

#for i in range(2): #range(numPredictors):
#    predictor=bpc.predictor(i+1)
#    predictor.plotPredictor(errorNorm)
#    
    

#%%
    
nLayers = len(numLayerNeurons)

wch=np.loadtxt('{}weight_distances.tsv'.format(path));# error=errordata[:,0]
wch1=wch[:,nLayers]
#wch2=wch[:]
#wch3=wch[:,2]
#maxW1=max(abs(wch[:,0])); maxW2=max(abs(wch[:,1])); maxW3=max(abs(wch[:,2]));
#maxW=max(maxW1,maxW2,maxW3)
#wch1=wch1/maxW1
#wch2=wch2/maxW2
#wch3=wch3/maxW3

wchfig=plt.figure('weigth change')
axe=wchfig.add_subplot(111)
plt.plot(wch1, color='black', linestyle="-", linewidth=0.5)
#plt.plot(wch2, color='black', linestyle="--", linewidth=0.5)
#plt.plot(wch3, color='black', linestyle="-.", linewidth=0.5)
#plt.grid(which='minor', color='grey', linestyle='--', linewidth=0.2)
#plt.ylabel('Error Signal')
#plt.ylim(-0.1, 1.1)
#plt.yticks([0,1])
#plt.xticks(np.arange(0,len(wch),250))
#axe.set_aspect(aspect=len(wch)/(1.2*1.5))
wchfig.savefig(spath+'weightchange', quality= 100, format='svg', bbox_inches='tight')
plt.show()

#%%

layer=bpc.layer(1)
layer.plotLayerWeights()

#for j in range(len(numLayerNeurons)):
#    for k in range(numLayerNeurons[j]):
#        neuron=bpc.neuron(int(str(j+1)+str(k+1)))
#        neuron.plotWeights()

#for n in range(len(numLayerNeurons)-1):
#    layer=bpc.layer(n+1)
#    layer.plotLayerWeights()
    
    
#%%
  
#finalLayer=bpc.finalLayer(len(numLayerNeurons))
#finalLayer.plotFinalLayerWeights()


