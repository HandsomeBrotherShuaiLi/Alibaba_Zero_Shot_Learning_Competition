from PIL import Image
import os
from imageai.Prediction import ImagePrediction
from imageai.Detection import ObjectDetection
import time
path="E:/DatasetA/"
train_data = os.listdir(path + 'train/')
pred = ImagePrediction()
detector = ObjectDetection()
pred.setModelTypeAsDenseNet()
detector.setModelTypeAsRetinaNet()
pred.setModelPath("./models/DenseNet-BC-121-32.h5")
detector.setModelPath("./models/resnet50_coco_best_v2.0.1.h5")
pred.loadModel()
detector.loadModel()
def func(num):
    image = Image.open(path + 'train/' + train_data[num])
    print('\n'+train_data[num])
    image.show()
    predections, prob = pred.predictImage("timg.jpg", result_count=5)
    detections = detector.detectObjectsFromImage(input_image="timg.jpg",
                                                 output_image_path="./new_image/new_timg.jpg")
    print("分类器结果：")
    for i, j in zip(predections, prob):
        print(i + ":" + j)
    print("__________________________________")
    print("切割器结果:")
    for e in detections:
        print(e['name'] + ":" + e['percentage_probability'])
    print("__________________________________")
func(1)