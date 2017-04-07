# process_logQ1test.py

import numpy as np
from collections import Counter

pathinput='./tests/test_features/log_input/log.txt'
datainput=open(pathinput,'r')

NoL=4400644 # wc -l log.txt 4400644

ipList=[]
for line in range(NoL):
    linetxt=datainput.readline()
    linetxtSplit=linetxt.split()
    host=linetxtSplit[0]
    ipstr=str(host)
    ipList.append(ipstr)
    
datainput.close()

ipList1=ipList[0:np.size(ipList):10]

#ipList1=ipList

ipCollcount=Counter(ipList1)   
ipActive10=Counter(ipCollcount).most_common(10)


pathTop10host='./tests/test_features/log_output/hosts.txt'
dataTop10host=open(pathTop10host,'wb')

for ipline in range(10):
    ipAcMost=ipActive10[ipline]
    hostname=ipAcMost[0]
    freq=ipAcMost[1]
    print hostname,",", freq
    dataTop10host.write('%s,%d\n' % (hostname,freq))

dataTop10host.close()


