import cv2
import numpy as np
from PIL import Image
from scipy import signal
from UI import Ui_MainWindow
from scipy.ndimage import filters
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton_27.setText('1.1 Load Image')
        self.ui.pushButton_27.clicked.connect(self.load_image)
        self.ui.pushButton_29.setText('1.2 Color Seperation')
        self.ui.pushButton_29.clicked.connect(self.color_seperation)
        self.ui.pushButton_28.setText('1.3 Color Transformations')
        self.ui.pushButton_28.clicked.connect(self.color_transforformations)
        self.ui.pushButton_15.setText('1.4  blending')
        self.ui.pushButton_15.clicked.connect(self.blending)
        self.ui.pushButton_17.setText('2.1 Gaussion Blur')
        self.ui.pushButton_17.clicked.connect(self.gaussion_blur_2_1)
        self.ui.pushButton_16.setText('2.2 Bilateral Filter')
        self.ui.pushButton_16.clicked.connect(self.bilateral_filter)
        self.ui.pushButton_25.setText('2.3 Median Filter')
        self.ui.pushButton_25.clicked.connect(self.median_filter)
        self.ui.pushButton_24.setText('3.1 Gaussion Blur')
        self.ui.pushButton_24.clicked.connect(self.gaussion_blur_3_1)
        self.ui.pushButton_18.setText('3.2 Sobel X')
        self.ui.pushButton_18.clicked.connect(self.sobel_x)
        self.ui.pushButton_26.setText('3.3 Sobel Y')
        self.ui.pushButton_26.clicked.connect(self.sobel_y)    
        self.ui.pushButton_19.setText('3.4 Magnitude')
        self.ui.pushButton_19.clicked.connect(self.magnitude)    
        self.ui.pushButton_20.setText('4.1 Resize')
        self.ui.pushButton_20.clicked.connect(self.resize_4_1)   
        self.ui.pushButton_21.setText('4.2 Translation')
        self.ui.pushButton_21.clicked.connect(self.translation)
        self.ui.pushButton_23.setText('4.3 Rotate Scalimg')
        self.ui.pushButton_23.clicked.connect(self.rotate_scaling)  
        self.ui.pushButton_22.setText('4.4 Shearing')
        self.ui.pushButton_22.clicked.connect(self.shearing)     
    def load_image(self):
        img = cv2.imread('Sun.jpg', 1)
        cv2.imshow('HW1-1', img)
        a,b,c=img.shape
        print("Height : "+str(a))
        print("Widht : "+str(b))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def color_seperation(self):
        img = cv2.imread('Sun.jpg', 1)
        B,R,G =cv2.split(img)
        zeros = np.zeros(img.shape[:2],dtype ="uint8")
        cv2.imshow("blue",cv2.merge([B,zeros,zeros]))
        cv2.imshow("green",cv2.merge([zeros,G,zeros]))
        cv2.imshow("red",cv2.merge([zeros,zeros,R]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def color_transforformations(self):
        image = cv2.imread('Sun.jpg')
        image1=[]
        image2=[]
        for i in range(len(image)):
            image3=[]
            image4=[]
            for j in range(len(image[0])):
                image3.append(np.uint8(image[i][j][0]*0.72+image[i][j][1]*0.21+image[i][j][2]*0.07))
                image4.append(np.uint8(image[i][j][0]/3+image[i][j][1]/3+image[i][j][2]/3))
            image1.append(image3)
            image2.append(image4)     
        image3=np.array(image1)    
        image4=np.array(image2)   
        cv2.imshow('L1', image4)
        cv2.imshow('L2', image3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def blending(self):      
        cv2.namedWindow('Blend')
        image1 = cv2.imread('Dog_Strong.jpg')
        image2 = cv2.imread('Dog_Weak.jpg')
        def update(x):          # 回调函数 更新value的值
            image3 = cv2.addWeighted(image1,1-(x/256),image2,x/256,0)
            cv2.imshow('Blend', image3)
        cv2.createTrackbar('Blend','Blend',0,255,update)        # 创建一个滑动条对象 数值名字叫做 value_name # 滑动条创建在 Blend 窗口之下 # 取值范围为 0-255, 回调函数为update
        cv2.waitKey(0)                                          
        cv2.destroyAllWindows()





    def gaussion_blur_2_1(self):
        image = cv2.imread("Lenna_WhiteNoise.jpg")
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        cv2.imshow("Gaussian", blurred)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    def bilateral_filter(self):   
        image = cv2.imread("Lenna_WhiteNoise.jpg")
        blurred = cv2.bilateralFilter(image, 9, 90, 90)
        cv2.imshow("Bilateral", blurred)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def median_filter(self):
        image = cv2.imread("Lenna_pepperSalt.jpg")
        image1=cv2.medianBlur(image, 3)
        image2=cv2.medianBlur(image, 5)
        cv2.imshow("Median Filter 3x3", image1)
        cv2.imshow("Median Filter 5x5", image2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    




    def gaussion_blur_3_1(self):
        img = cv2.imread('House.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x, y = np.mgrid[-1:2, -1:2]
        gaussian_filter = np.exp(-(x**2 + y**2))
        gaussian_filter = gaussian_filter / gaussian_filter.sum()
        gaussian_blur = signal.convolve2d(gray, gaussian_filter, boundary='symm')
        gaussian_blur = gaussian_blur.astype(np.uint8)
        cv2.imshow("Gaussian Blur", gaussian_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def sobel_x(self):
        img = cv2.imread('House.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x, y = np.mgrid[-1:2, -1:2]
        gaussian_filter = np.exp(-(x**2 + y**2))
        gaussian_filter = gaussian_filter / gaussian_filter.sum()
        gaussian_blur = signal.convolve2d(gray, gaussian_filter, boundary='symm')
        gaussian_blur = gaussian_blur.astype(np.uint8)
        sobel_x_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_x = signal.convolve2d(gaussian_blur, sobel_x_filter, boundary = 'symm')
        sobel_x = np.abs(sobel_x)
        sobel_x [ sobel_x > 255 ] = 255
        result = sobel_x.astype(np.uint8)
        cv2.imshow("Sobel X", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def sobel_y(self): 
        img = cv2.imread('House.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x, y = np.mgrid[-1:2, -1:2]
        gaussian_filter = np.exp(-(x**2 + y**2))
        gaussian_filter = gaussian_filter / gaussian_filter.sum()
        gaussian_blur = signal.convolve2d(gray, gaussian_filter, boundary='symm')
        gaussian_blur = gaussian_blur.astype(np.uint8)
        y_filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        sobel_y = signal.convolve2d(gaussian_blur, y_filter, boundary = 'symm')
        sobel_y = np.abs(sobel_y)
        sobel_y [ sobel_y > 255 ] = 255
        result = sobel_y.astype(np.uint8)
        cv2.imshow("Sobel Y", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    

    def magnitude(self):
        img = cv2.imread('House.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x, y = np.mgrid[-1:2, -1:2]
        gaussian_filter = np.exp(-(x**2 + y**2))
        gaussian_filter = gaussian_filter / gaussian_filter.sum()
        gaussian_blur = signal.convolve2d(gray, gaussian_filter, boundary='symm')
        gaussian_blur = gaussian_blur.astype(np.uint8)

        y_filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        sobel_y = signal.convolve2d(gaussian_blur, y_filter, boundary = 'symm')
        sobel_y = np.abs(sobel_y)
        sobel_y [ sobel_y > 255 ] = 255

        x_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_x = signal.convolve2d(gaussian_blur, x_filter, boundary = 'symm')
        sobel_x = np.abs(sobel_x)
        sobel_x [ sobel_x > 255 ] = 255

        sobel = (sobel_x **2+ sobel_y **2) **0.5
        sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
        sobel = sobel.astype(np.uint8)
        cv2.imshow("Sobel", sobel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
     



     
    def resize_4_1 (self):
        image = cv2.imread('SQUARE-01.png')
        image2 = cv2.resize(image, (256, 256))
        cv2.imshow('Img_1', image2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def translation(self):
         image = cv2.imread("SQUARE-01.png")
         image =cv2.resize(image,(256,256))
         h=np.float32([[1,0,0],[0,1,60]])
         image=cv2.warpAffine(image,h,(400,300))
         cv2.imshow("Img_2", image)
         cv2.waitKey(0)
         cv2.destroyAllWindows()

    def rotate_scaling(self): 
        image = cv2.imread("SQUARE-01.png")
        image = cv2.resize(image, (300, 300))
        (h, w) = image.shape[:2]
        # 若未指定旋转中心，则将图像中心设为旋转中心
        center = (w / 2, h / 2)
        # 执行旋转
        M = cv2.getRotationMatrix2D(center, 10, 0.5)
        image = cv2.warpAffine(image, M, (400, 300))
        cv2.imshow("Img_3", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def shearing(self):
        image = cv2.imread("SQUARE-01.png")
        image =cv2.resize(image,(150,150))
        h=np.float32([[1,0,60],[0,1,100]])
        image=cv2.warpAffine(image,h,(400,300))
        m1= np.float32([[50,50],[200,50],[50,200]])
        m2= np.float32([[10,100],[200,50],[100,250]])
        m=cv2.getAffineTransform(m1,m2)
        image=cv2.warpAffine(image,m,(400,300))
        cv2.imshow("image_2", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':                           #start
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow_controller()
        window.show()
        sys.exit(app.exec_())   
