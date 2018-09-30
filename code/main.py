import os
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from collections import defaultdict
f=open("../data/DatasetB/label_list.txt").readlines()
ans=defaultdict(set)
for line in f:
    temp=line.split('\t')
    zj=temp[0]
    en=temp[1]
    enlist=en.strip('\n').strip(' ').strip('\t').split(',')
    for j in enlist:
        tt=j.strip(' ').split(' ')
        if len(tt)>1:
            tt='_'.join(tt)
        else:
            tt=tt[0]
        ans[zj].add(tt)
for i in ans.keys():
    print(i,ans[i])

model1=gensim.models.KeyedVectors.load('../data/External/google_news.model')

model2=gensim.models.KeyedVectors.load('../data/External/raw.model')
model3=gensim.models.KeyedVectors.load('../data/External//en.model')
comp=open("../data/External/wordebedding.txt").readlines()
print('read data!')
res={}
result=open('../submit/predection_v3.txt','w',encoding='utf-8')
n=0
for i in comp:
    n+=1
    t=i.strip('\n').split('\t')
    jpg=t[0]
    maxProb=0
    for zj in ans.keys():
        similabel=ans[zj]
        sumlabel=0
        for p in t[1:]:
            pname=p.strip('\n').strip('\t').split('%')
            pre=pname[0]
            prob=float(pname[1])
            for en in similabel:
                try:
                    sumlabel += model1.similarity(en, pre) * prob
                except KeyError:
                    sumlabel += prob * 0.2
                try:
                    sumlabel += model2.similarity(en, pre) * prob
                except KeyError:
                    sumlabel += prob * 0.2
        sumlabel = 1.0 * sumlabel / len(similabel)
        if sumlabel>maxProb:
            res[t[0]]=zj
            maxProb=sumlabel
    print(n,t[0]+'\t'+res[t[0]]+'\t'+str(maxProb))
    result.write(t[0]+'\t'+res[t[0]]+'\n')
result.close()