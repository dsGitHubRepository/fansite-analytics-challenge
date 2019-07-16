# process_logQ1.py

NoL=4400644 # wc -l log.txt 4400644

from collections import Counter
data = open('../log_input/log.txt', 'r')

ActiveHost = []

for i in range(200000):
    l1 = data.readline().split('- -')[0]
    ActiveHost.append(l1)
data.close()
print(ActiveHost[0:2])

top10 = Counter(ActiveHost).most_common(10)

file = open('../log_output/top.txt', 'w')

for i in range(10):
    ip = top10[i][0]
    freq = top10[i][1]
    print(type(freq))
    file.write('%s,%d\n' % (ip,freq))

file.close()
