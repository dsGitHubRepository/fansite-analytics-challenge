# process_logQ2test.py

import numpy as np
import pandas as pd

pathinput='./tests/test_features/log_input/log.txt'
datainput=open(pathinput,'r')

NoL=44006  # wc -l log.txt 4400644
# for quick check a portion of the input can be chosen

byteList=[]
rsrcList=[]

for line in range(NoL):
    linetxt=datainput.readline()
    linetxtSplit=linetxt.split()
    if np.size(linetxtSplit)==10 :
        if linetxtSplit[9] != str('-'):
            rsrc=linetxtSplit[6]
            rsrcstr=str(rsrc)
            rsrcList.append(rsrcstr)
            q2byte=linetxtSplit[9]
            byteList.append(q2byte)

# Remove duplicate item from the list                        
rsrcNodupl=list(set(rsrcList))

lprog=np.size(rsrcNodupl)/10
bandwidthList=[]
for lsrc1 in range(np.size(rsrcNodupl)):
    if lsrc1%lprog == 0:  
        print "progress : ", lsrc1/lprog   
    srcitem1=rsrcNodupl[lsrc1]
    srcitem1str=str(srcitem1)  # to be sure
    nc=0
    sumbyte=0 
    for lsrc2 in range(np.size(rsrcList)):  
        srcitem2str=rsrcList[lsrc2] 
        if srcitem1str==srcitem2str:
             idxstr=str(lsrc2)
             sumbyte=sumbyte+int(byteList[lsrc2])
             nc=nc+1    # repeated resources count
        sumbytePerfreq=sumbyte/(nc+1) # average out
    bandwidthList.append(sumbytePerfreq)
    
bandwListint=list(map(int,bandwidthList))

pathoutRsrc='./tests/test_features/log_output/resources.txt'
dataoutRsrc=open(pathoutRsrc,'wb')

for irsrc in range(10):
    RsrcMaxbw=max(bandwListint)
    idxMaxbw=pd.Series(bandwListint).idxmax()
    topMostRsrc=rsrcNodupl[idxMaxbw+irsrc]     # since the top resources was not dropped in loop iteration
    dataoutRsrc.write('%s \n' % topMostRsrc)
    print "\n top", irsrc+1, ":", topMostRsrc, "bandwidth : ", RsrcMaxbw
    bandwListint.remove(max(bandwListint))     # max bandwidth was dropped during iteration
       
dataoutRsrc.close()
