# #1.提取所有的英文字符
# f=open("D:/DatasetB_20180919/label_list.txt").readlines()
# en=open("D:/DatasetB_20180919/label_en_list.txt",'w')
# zj=open("D:/DatasetB_20180919/label_zj_list.txt",'w')
# for i in f:
#     temp=i.strip('\n').strip(' ').strip('\t').split('\t')
#     print(temp)
#     en.write(temp[1]+'\n')
#     zj.write(temp[0]+'\n')
# en.close()
# zj.close()

from tkinter import *
from PIL import Image,ImageTk
flag=False
class W(object):
    def __init__(self):
        self.data=open("D:/DatasetB_20180919/image.txt").readlines()

        self.count=706
        temp=open("pred/predection_2model_newlabels_140_copy.txt").readlines()
        self.res={}
        self.result=open("pred/predection_newlabels_magic.txt","w")
        for i in temp:
            t=i.strip('\n').strip('\t').split("\t")
            self.res[t[0]]=t[1]


    def start(self):
        self.root = Tk()
        self.root.geometry('400x200')
        self.root.resizable(width=False, height=False)
        im = Image.open("D:/DatasetB_20180919/test/" + self.data[self.count].strip('\n').strip('\t'))
        print(self.data[self.count].strip('\n').strip('\t'))
        img = ImageTk.PhotoImage(im)
        imlabel = Label(self.root, image=img).pack()
        textLabel = Label(self.root, text="ZJL").pack()
        self.textstr = StringVar()
        textEnt = Entry(self.root, textvariable=self.textstr)
        # print(textstr.get())
        self.textstr.set("")
        textEnt.pack()
        but = Button(self.root, text="next", command=self.next_jpg).pack()
        self.root.mainloop()


    def next_jpg(self):
        self.count+=1

        if self.textstr.get()!="":
            self.res[self.data[self.count-1].strip('\n').strip('\t')]='ZJL'+self.textstr.get()
        self.result.write(self.data[self.count-1].strip('\n').strip('\t')+'\t'+self.res[self.data[self.count-1].strip('\n').strip('\t')]+'\n')
        self.root.destroy()
        self.start()



if __name__=="__main__":
    h=W()
    h.start()


