from tkinter import *
from tkinter import messagebox
import os
import random

class qunarCrawlGui():
    def __init__(self) -> None:
        self.root=Tk()
        self.root.geometry("600x400+300+200")
        self.root.title("旅游数据爬虫")
        self.__addButton()
        self.__addLabel()
    def __addLabel(self):
        lab1=Label(self.root,text='Welcome!',font=("宋体",30),fg='red')
        lab1.grid(row=0,column=5)
    def __addButton(self):
        btn1=Button(self.root,text='数据爬取',command=self.runBtn1)
        btn2=Button(self.root,text="数据处理",command=self.runBtn2)
        btn1.grid(row=1,column=3)
        btn2.grid(row=1,column=6)
    def runBtn1(self):
        # os.chdir()
        os.system('python -u qunar.py')
    def runBtn2(self):
        os.system('python -u processHotel.py')
    def start(self):
        self.root.mainloop()
        
root=qunarCrawlGui()
root.start()