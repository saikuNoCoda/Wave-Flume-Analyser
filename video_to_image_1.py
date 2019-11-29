import cv2
import os

cam = cv2.VideoCapture("x.MOV")
cam.set(cv2.CAP_PROP_POS_MSEC,200) 

try:
	if not os.path.exists('data1'):
		os.makedirs('data1')
except OSError:
	print('Error: Creating directory of data1')

currentframe = 0

while(True):

	ret,frame = cam.read()

	if(ret):
		name = './data1/' + str(currentframe) + '.jpg'
		print('Creating...' + name)

		cv2.imwrite(name,frame)
		currentframe += 1
	else:
		break

cam.release()
cv2.destroyAllWindows()