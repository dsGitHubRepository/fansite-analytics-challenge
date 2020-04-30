# process_logQ4.py

import numpy as np
from collections import Counter
from itertools import groupby
from operator import itemgetter
import datetime


pathinput='./log_input/log.txt'
datainput=open(pathinput,'r')

# wc -l log.txt 4400644
NoL=4400644 # 4400644

ipList1=[]
httpreplyList1=[]
tstmpList1=[]
rsrcList=[]

nc=0
for line1 in range(NoL):
    linetxt1=datainput.readline()
    linetxtSplit1=linetxt1.split()
    if  np.size(linetxtSplit1)==10 :
        httpcode=linetxtSplit1[8]          
        if (httpcode =='200' or httpcode=='401' or httpcode=='304'):
            ip1=linetxtSplit1[0] 
            ipList1.append(ip1)                # hostlist
            HTTPrep=linetxtSplit1[8]        
            httpreplyList1.append(HTTPrep)     # httpReplyCodeList
            tstmp=linetxtSplit1[3] 
            tstmpstr=str(tstmp[1:21])
            tstmpList1.append(tstmpstr)        # timestampList
            rsrc=linetxtSplit1[6]
            rsrcList.append(rsrc) 
             
datainput.close()

# httpreplyList1 contains codes '200=success', '401=blocked' and '304'=forbiddn 

httpIndex401=[]
for hi,hj in enumerate(httpreplyList1):
    if hj =='401':
        httpIndex401.append(hi)  # index list
        
# Index list for failed logon

pathblockedout='./log_output/blocked.txt'
datablockedout=open(pathblockedout,'wb')

FMT= '%d/%b/%Y:%H:%M:%S'  # timestamp format for the input data

# Since we are searching for multiple consecutive '401' failed attempt;
# indices for '401' be checked for consecutive order
 
# 







datablockedout.close()                               
                            
                            

