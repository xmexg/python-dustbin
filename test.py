#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter  # 导入 Tkinter 库
import numpy as np
from PIL import Image as PILImg
from PIL.ImageQt import ImageQt
from matplotlib import image as matimg
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QImage


# 演示创建窗口
def show_window():
    root = tkinter.Tk()  # 创建窗口对象的背景色
    # 创建两个列表
    li = ['C', 'python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']
    listb = tkinter.Listbox(root)  # 创建两个列表组件
    listb2 = tkinter.Listbox(root)
    for item in li:  # 第一个小部件插入数据
        listb.insert(0, item)

    for item in movie:  # 第二个小部件插入数据
        listb2.insert(0, item)

    listb.pack()  # 将小部件放置到主窗口中
    listb2.pack()
    root.mainloop()  # 进入消息循环,显示窗口


def show_win_map():
    app = QApplication(sys.argv)  # 创建一个应用对象,sys.argv是一个命令行参数列表
    widget = QWidget()  # 创建一个窗口对象
    grid = QGridLayout()  # 创建一个网格布局

    image1 = QPixmap("img/map.png")  # 创建一个图片对象
    label1 = QLabel(widget)  # 创建一个标签对象
    label1.setPixmap(image1)  # 设置标签的图片

    image2 = QPixmap("img/map.png")  # 创建一个图片对象
    label2 = QLabel(widget)  # 创建一个标签对象
    npImg = np.array(image2)  # 将图片转换为数组
    img = PILImg.open("img/map.png")  # 读取图片
    arr = np.array(img)  # 将图片转换为数组
    arr[(arr != [255, 255, 255]).all(axis=2)] = [0, 0, 0]  # 将非白色的像素点设置为黑色
    img_rgb = PILImg.fromarray(arr)  # 将数组转换为图片

    q_image = QImage(img_rgb.tobytes(), img_rgb.size[0], img_rgb.size[1], QImage.Format_RGB888)
    label2.setPixmap(QPixmap.fromImage(q_image))  # 设置标签的图片

    grid.addWidget(label1, 0, 0)  # 将标签添加到网格布局中,并设置其在0行0列的位置
    grid.addWidget(label2, 0, 1)  # 将标签添加到网格布局中,并设置其在0行1列的位置
    widget.setLayout(grid)  # 设置窗口的布局
    widget.setGeometry(50, 50, 640, 640)  # 设置窗口的位置和大小,
    widget.setWindowTitle("地图二值化")  # 设置窗口的标题
    widget.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入消息循环
