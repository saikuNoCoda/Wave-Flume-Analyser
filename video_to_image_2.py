import cv2
import os

cam = cv2.VideoCapture("xx.mp4")
cam.set(cv2.CAP_PROP_POS_MSEC,200) 

try:
	if not os.path.exists('data2'):
		os.makedirs('data2')
except OSError:
	print('Error: Creating directory of data1')

currentframe = 0

while(True):

	ret,frame = cam.read()

	if(ret):
		name = './data2/' + str(currentframe) + '.jpg'
		print('Creating...' + name)

		cv2.imwrite(name,frame)
		currentframe += 1
	else:
		break

cam.release()
cv2.destroyAllWindows()
