# process_logQ3.py

import numpy as np
import pandas as pd
import datetime

pathinput='./log_input/log.txt' 
datainput=open(pathinput,'r')

NoL=4400644 #  wc -l log.txt 4400644

lprog=int(NoL/10)

tstpList1=[]

for line in range(NoL):
    linetxt=datainput.readline()
    linetxtSplt=linetxt.split()
    q3txttstp=linetxtSplt[3]   # timestamp 
    q3txttstpp=q3txttstp[1:21]
    tstpList1.append(q3txttstp[1:21])   # duplicated timestamp
        
datainput.close()

delta=200
tstpList=tstpList1[0:np.size(tstpList1):delta]
# here I am choosing datastep delta=200 for time managable analysis. Higher steps produce results that is more spaced
# in real time. default delta=1; More time managed approach would be useful to filter input initially only for http reply code '200'
# please check results at /fansite-analytics-challenge/insight_testsuite/tests/test_features/log_output/hours.txt for very wide datastep
# delta=40000; 

tstpListNoDup=list(set(tstpList))     # remove duplicate items 
tstpListNoDup.sort()   

# set 60 minute time window and get frequency for each unique(unduplicatedlist) timestamp
# 
freq1=[]
FMT= '%d/%b/%Y:%H:%M:%S'

lprog=np.size(tstpListNoDup)/10

for line1 in range(np.size(tstpListNoDup)): 
    if line1%lprog == 0: 
        print "progress : ", line1/lprog 
    time1=tstpListNoDup[line1]
    n=0
    for line2 in range(np.size(tstpListNoDup)): 
        if line1<line2:                    # compare one wrt raming all
            time2=tstpList[line2]
            if time1 < time2:              # since we look for real time window
                timeDiff=datetime.datetime.strptime(time2, FMT) - datetime.datetime.strptime(time1,FMT)
                tt=timeDiff.seconds 
                if tt <= 3600 :   # 60 min = 3600 s
                    n=n+1   # count freq for 60 min window
    freq1.append(n)    
freq=list(map(int, freq1)) 
pathoutbusytime='./log_output/hours.txt'
dataouthrs=open(pathoutbusytime,'wb')                                

for ifrq in range(10):
    m=max(freq)
    index=pd.Series(freq).idxmax()  # work for int list
    busiesttime=tstpListNoDup[index+ifrq]
    dataouthrs.write('%s %s\n' % (busiesttime, "-0400"))
    print busiesttime,"-0400",",", m
    freq.remove(max(freq))
dataouthrs.close()    
    
    

