# NDVI.py

import numpy as np
import matplotlib.pyplot as plt 
import os


# banda1 = np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band1_clip.npy')
# plt.imshow(banda1, vmin = 0, vmax = 2)
# plt.hist(banda1.flatten(),bins=100)


#%%
def crear_img_png(carpeta, banda):
    files = os.listdir(carpeta)
    data_banda = []
    for file in files:
        if file[-10:] == (str(banda)+'_clip.npy'):
            data_banda = np.load('clip/'+file)
            break
    
    fig, ax1= plt.subplots()
    pos = ax1.imshow(data_banda, vmin = 0, vmax = 2)
    fig.colorbar(pos, ax=ax1)
    plt.show()
    
    plt.savefig('clip/'+file[:-4]+'.png')
    
#%%
def crear_hist_png(carpeta, banda, bins):
    files = os.listdir(carpeta)
    data_banda = []
    for file in files:
        if file[-10:] == (str(banda)+'_clip.npy'):
            data_banda = np.load('clip/'+file)
            break

    plt.figure()
    plt.hist(data_banda.flatten(),bins=bins)
    plt.savefig('clip/'+file[:-4]+'_histograma.png')
    plt.show()
    
#%%
for i in range(1,8):
    crear_img_png('clip', i)
    crear_hist_png('clip', i, 100)

            
            
            