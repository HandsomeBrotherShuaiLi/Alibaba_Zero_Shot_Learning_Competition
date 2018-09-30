from imageai.Prediction import ImagePrediction
import os
data={}
f=open("E:/DatasetA/label_list.txt").readlines()
for i in f:
    zj=i.strip('\n').split('\t')[0]
    la=i.strip('\n').split('\t')[1]
    data[zj]=la
pred=ImagePrediction()
pred.setModelTypeAsDenseNet()
pred.setModelPath("models/DenseNet-BC-121-32.h5")
pred.loadModel()
train=open("E:/DatasetA/train.txt").readlines()
acc=0
n=0
for index,i in enumerate(train):
    n+=1
    path=i.strip('\n').split('\t')[0]
    label=i.strip('\n').split('\t')[1]
    flag=0
    predictions, probabilities = pred.predictImage("E:/DatasetA/train/"+path, result_count=1000)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        if eachPrediction in data.values():
            flag=1
            # print(eachPrediction + " : " + eachProbability)
            # print("true label",data[label])
            if eachPrediction==data[label]:
                acc+=1
            else:
                pass
            break
    if flag==0:
        pass
    if index%10==0:
        print(index,1.0*acc/n)





# # import json
# # data={}
# # f=open("E:/DatasetA_test_20180813/DatasetA_test/label_list.txt").readlines()
# # for i in f:
# #     zj=i.strip('\n').split('\t')[0]
# #     la=i.strip('\n').split('\t')[1]
# #     data[zj]=la
# # with open("class.json",'w') as f1:
# #     json.dump(data,f1)

# f=open("pred/submit_v2.txt").readlines()
# print(f)