import numpy as np
import skimage
import matplotlib.pyplot as plt
import cv2
import os
import scipy.misc as sm
import os.path
from PIL import Image
import xlwt
from xlwt import Workbook


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

list1 = []
list2 = []

def resize_image(dir_name):
	DIR = dir_name
	length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	
	for i in range(length):
		foo = Image.open(DIR+"/"+str(i)+".jpg")
		foo = foo.resize((120,120),Image.ANTIALIAS)
		foo.save(DIR+"/"+str(i)+".jpg",quality=95)

def load_data(dir_name):
	DIR = dir_name
	length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

	imgs = []

	for i in range(length):
		img = cv2.imread(DIR+"/"+str(i)+".jpg",0)
		imgs.append(img)

	print(imgs[0].shape)
	return imgs

def threasholding_images(imgs):

	imgs_n = []
	for img in imgs:
		ret,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		img = 255 - img
		# FOR EDGE DETECTION
		# img = cv2.Canny(img,0,255,10)
		imgs_n.append(img)

	plt.imshow(imgs_n[0],cmap='gray')
	plt.show()
	return imgs_n

def save_images(dir_name,imgs):
	try:
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
	except OSError:
		print('Error creating ' + dir_name)

	for i,img in enumerate(imgs):
		name = "./" + dir_name + "/frame" + str(i) + ".jpg"
		cv2.imwrite(name,img)


def generate_video(images,type):
    image_folder = 'reqdata1' 
    video_name = 'output1.avi'

    if(type == 2):
		image_folder = 'reqdata2' 
		video_name = 'output2.avi'

    frame = np.uint8(cv2.merge((images[0],images[0],images[0])))
  	
    height, width, layers = frame.shape
    mid = 30
    SIZ = 3
    video = cv2.VideoWriter(video_name, 0, 20, (width, height))

    base_height = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    pp = 1
    for image in images:
    	x = 0
    	for i in range(height):
    		if(max(image[i,mid-SIZ:mid+SIZ+1]) == 255):
    			x = height - i
    			break
    	if(base_height == 0):
    		base_height = x
    	orig_height = 28.0/base_height
    	orig_height = orig_height*x

    	xorig = 0
    	if(base_height < 0 or base_height >= 0):
    		for i in range(int(base_height+30),0,-1):
    			print(i)
	    		if(max(image[i,mid-SIZ:mid+SIZ+1]) == 0):
	    			x = height - i
	    			break
	    	if(base_height == 0):
	    		base_height = x
	    	xorig = 28.0/base_height
	    	xorig = xorig*x

		orig_height = (xorig + orig_height)/2.0


    	sheet1.write(pp,type-1,orig_height-28.0)
    	if(type == 1):
    		list1.append(orig_height-28.0)
    	else:
    		list2.append(orig_height-28.0)
    		
        pp = pp + 1
        new_image = cv2.merge((image,image,image))
    	cv2.putText(new_image,str(orig_height-28.0),(30,30),font,1,(255,255,255),2,cv2.LINE_AA)
    	cv2.putText(new_image,".",(mid,height-x),font,1,(255,0,0),2,cv2.LINE_AA)
    	
    	video.write(np.uint8(new_image))

    cv2.destroyAllWindows()  
    video.release() 

resize_image("data1")
imgs = load_data("data1")
imgs = threasholding_images(imgs)
save_images("req_data1",imgs)
generate_video(imgs,1)

# resize_image("data2")
# imgs = load_data("data2")
# imgs = threasholding_images(imgs)
# save_images("req_data2",imgs)
# generate_video(imgs,2)

wb.save('waves.xls')