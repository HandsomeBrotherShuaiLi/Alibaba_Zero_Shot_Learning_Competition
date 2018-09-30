import gensim
import logging
import matplotlib.pyplot as plt
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model=gensim.models.Word2Vec.load("C:/Xilinx/Tale.of.Wuxia.The.Pre.Sequel.v1.0.1.4-ALI213/en_1000_no_stem/en.model")
print(model.similarity('dog','cat'))
# # # model=gensim.models.KeyedVectors.load_word2vec_format("dictionary/GoogleNews-vectors-negative300.bin",binary=True)
# # # model.save('models/google_news.model')
# # model1=gensim.models.KeyedVectors.load('models/google_news.model')
# #
# # # model2=gensim.models.KeyedVectors.load('models/craw.model')
# #
# # f=open("E:/DatasetA_test_20180813/DatasetA_test/label_list.txt").readlines()
# # comp=open("models/train_pred/train_prediction.txt").readlines()
# # ans={}
# # result=open('pred/train_result.txt','w',encoding='utf-8')
# # acc=0
# # kk=0
# # x=[]
# # y=[]
# # for location,i in enumerate(comp):
# #     t=i.strip('\n').split('\t')
# #     maxProb=0
# #     kk+=1
# #     # print("t是",t)
# #     for label in f:
# #         temp=label.strip('\n').split('\t')
# #         zj=temp[0]
# #         enname=temp[1]
# #         sumlabel=0
# #         for p in t[2:]:
# #             pname=p.split('&&')
# #             # print("pname",pname)
# #             p1=' '.join(pname[:-1])
# #             p1=p1.split('_')
# #             p2=' '.join(p1)
# #             # print("p2",p2)
# #             prob=float(pname[-1])
# #             # print("prob",prob)
# #             # try:
# #             #     sumlabel += model2.similarity(enname, p2) * prob
# #             # except KeyError:
# #             #     sumlabel+=prob*0.25
# #             try:
# #                 sumlabel += model1.similarity(enname, p2) * prob
# #             except KeyError:
# #                 sumlabel+=prob*0.2
# #
# #         if sumlabel>maxProb:
# #             ans[t[0]]=zj
# #             maxProb=sumlabel
# #     print(location,t[0],ans[t[0]],t[1],maxProb)
# #     if t[1]==ans[t[0]]:
# #         acc+=1
# #     # result.write(t[0]+'\t'+ans[t[0]]+'\t'+t[1]+'\n')
# #     if(kk%10==0):
# #         y.append(1.0 * acc / kk)
# #         x.append(kk)
# #         print("acc", 1.0 * acc / kk)
# #
# #
# # print("final acc",1.0*acc/kk)
# # result.close()
# # plt.plot(x, y, marker='.',color='red')
# # plt.title("val acc")
# # plt.savefig('PHOTO/acc.png')
# #
# #
# # # f=open("models/resultfinall3.txt").readlines()
# # # print(f)
#
# test=open("E:/DatasetA_test_20180813/DatasetA_test/image.txt").readlines()
# f=open("pred/submit_v2.txt",'w')
# su=open('pred/submit.txt').readlines()
# final3=open('models/final3.txt').readlines()
# for i in su:
#     temp=i.split('\t')[0]+'\n'
#     if temp in test:
#         f.write(i)
# f.close()
# f=open("pred/submitall3_v2.txt",'w')
# for i in final3:
#     temp=i.split('\t')[0]+'\n'
#     if temp in test:
#         f.write(i)
# f.close()

