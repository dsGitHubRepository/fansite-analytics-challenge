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
 
for ncomp, h in groupby(enumerate(httpIndex401), lambda (i, x): i-x):
    Indexhttpgroup=map(itemgetter(1), h)        # consecutive indexList[] 
    SizeIndexgroup=np.size(Indexhttpgroup)      
    CFS=4   # CFS = consecutive failed attempts: 3 times or 4 times etc
    if SizeIndexgroup==CFS:
        ipRecall=[]
        for index in Indexhttpgroup:
            ipRecall.append(ipList1[index])  
            count=Counter(ipRecall)  
            ipSize=np.size(ipRecall)
            CountMostcommon=count.most_common() 
            ipwithIndex=CountMostcommon[0] 
            FofR=ipwithIndex[1]    # to make sure taht successive '401' from the same ip; 
            ipcheck1=ipwithIndex[0]
            if ipSize==FofR:   # test for ip uniqueness
                if FofR==CFS:
                    t1index=Indexhttpgroup[0] 
                    time1=tstmpList1[t1index]   # timestamp for 1st failed attemp
                    t2index=Indexhttpgroup[CFS-1]   
                    time2=tstmpList1[t2index]   # timestamp for Nth=(NOSFA)-th failed attemp
                    timeDiff=datetime.datetime.strptime(time2, FMT) - datetime.datetime.strptime(time1,FMT)
                    timeDiffSec=timeDiff.seconds
                    #print "timeDiffsec", timeDiffSec
                    timeStep=5     # Nth failed attempt over timeStep (20 sec or 5 sec etc)
                    nt=0
                    if timeDiffSec==timeStep:   # timedifference for successive failed attempt 
                        immediateIndex=t2index+1
                        npSizehttpreplyList1=np.size(httpreplyList1)
                        for icode in range(immediateIndex,npSizehttpreplyList1):
                            httpi=httpreplyList1[icode]
                            ipcheck2=ipList1[icode]
                            if (httpi=='304' and ipcheck1==ipcheck2): # to make sure that it is from the same ip
                                index304=icode
                                time1_304=tstmpList1[index304]
                                timeDelta=datetime.datetime.strptime(time1_304, FMT) - datetime.datetime.strptime(time2,FMT)
                                timeDeltaseconds=timeDelta.seconds
                                #print timeDeltaseconds
                                timestepBlock=300   # 5 minutes etc
                                if timeDeltaseconds<=timestepBlock:
                                    print  ipList1[icode],"--",tstmpList1[icode],";",httpreplyList1[icode]
                                    datablockedout.write('%s %s %s %s %s %s\n' % (ipList1[icode],"--",\
                                    tstmpList1[icode],";",rsrcList[icode], httpreplyList1[icode]))
                                    
                                    
                                
datablockedout.close()                               
                            
                            

