import os
import numpy as np
from shutil import copyfile


ESD_path = '/Users/liurui/WorkSpace/DATA_Resource/HLT-ESD/HLT-ESD/'
spklist = ['0011','0012','0013','0014','0015','0016','0017','0018','0019','0020']
emos = ['Angry','Happy','Sad','Angry','Surprise','Neutral']
newdir_path = '/Users/liurui/WorkSpace/OneDrive/SUTD_OneDrive/OneDrive - Singapore University of Technology and Design/Interspeech2021/ESS/ETTS-demo/ESD-sample/'

def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
        
            newDir=os.path.join(dir,s)
            get_filelist(newDir, Filelist)
    return Filelist
 
for spk in spklist:
    for emo in emos:
    	# os.mkdir(ESD_path + spk)
        wavlist = get_filelist(ESD_path+'/'+spk+'/'+emo, [])
        # print('------'+str(len(wavlist)))
        # wavlist = sorted(wavlist)
        new_path  = newdir_path +'/'+spk + '/'+ wavlist[0][-15:]
        print(new_path)
        copyfile(wavlist[0], new_path)