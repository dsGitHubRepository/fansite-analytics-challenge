# process_logQ4.py

import numpy as np
from collections import Counter

pathinput='./log_input/log.txt'
# 
# wc -l 4400644
datainput=open(pathinput,'r')

NoL=44000 # 4400644   # 4400644


ipList1=[]
httpreplyList1=[]
tstmpList1=[]
for line1 in range(NoL):
    linetxt1=datainput.readline()
    linetxtSplit1=linetxt1.split()
    httpCond=linetxtSplit1[8] 
    if (np.size(linetxtSplit1)==10 and (httpCond=='403' or httpCond=='200')) :
        eachip1=linetxtSplit1[0]          # ip
        ipList1.append(eachip1)
        HTTPrep=linetxtSplit1[8]          # httpRelpyCode
        httpreplyList1.append(HTTPrep)
        tstmp=linetxtSplit1[3] # time stamp
        tstmpstr=str(tstmp[1:21])
        tstmpList1.append(tstmpstr)
        
datainput.close()


ipList=ipList1   # [0:np.size(ipList1):delta]
httpreplyList=httpreplyList1 #    [0:np.size(httpreplyList1):delta]
tstmpList=tstmpList1    # [0:np.size(tstmpList1):delta]

print ipList[0:4]; print httpreplyList; print tstmpList[0:4]

# get ipUnDup list

ipListCounter=Counter(ipList); #print ipListCounter  
nAc=3
ipListCounMostAc=Counter(ipList).most_common(nAc); #print "Top:", ipListCounMostAc

for i,j in enumerate(ipList):
    ip1=ipList[0]
    n=0
    if j==ip1:
        print i 
        ii=int(i)



 

