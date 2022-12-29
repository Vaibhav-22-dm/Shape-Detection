'''
*****************************************************************************************
*
*        		===============================================
*           		Berryminator (BM) Theme (eYRC 2021-22)
*        		===============================================
*
*  This script is to implement Task 1A of Berryminator(BM) Theme (eYRC 2021-22).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ 2248 ]
# Author List:		[ Vaibhav Mohite, Tejas Ambhore, Harsh Wasnik, Harsh Verma ]
# Filename:			task_1a.py
# Functions:		detect_shapes, get_labeled_image
# 					[ Comma separated list of functions in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_shapes(img):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list
	containing details of colored (non-white) shapes in that image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	Returns:
	---
	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image
	
	Example call:
	---
	shapes = detect_shapes(img)
	"""    
	detected_shapes = []

	##############	ADD YOUR CODE HERE	##############	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hsv_codes = [
			['Red', [0,100,100], [10, 255, 255]],
			['Blue', [110, 100,100], [130, 255, 255]],
			['Green', [50, 100,100], [70, 255, 255]],
			['Orange', [10, 100, 20], [25, 255, 255]],
		]

	# Loop through all the colors in order to find shapes of each color - 
	for i in range(0, len(hsv_codes)):
		# Detecting shapes of ith color
		lower_range = np.array(hsv_codes[i][1])
		upper_range = np.array(hsv_codes[i][2])

		mask = cv2.inRange(hsv, lower_range, upper_range)

		if(mask.any()): 
			color = hsv_codes[i][0]
		else:
			continue

		threshold , thresh = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
		contours, heirarchies = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		for contour in contours:
			approx = cv2.approxPolyDP(contour, 0.019*cv2.arcLength(contour, True), True)
			temp = [0, 0, 0, 597, 897, 597, 897, 0]
			flag = 0
			for i in range(len(approx.ravel())):
				if temp[i] != approx.ravel()[i]:
					flag = 1 
					break
			if flag:
				shapeName = 'Circle'
				zs = list(approx.ravel())
				xcoords = [j for i, j in enumerate(zs) if i%2==0]
				xcoords.sort()
				ycoords = [j for i, j in enumerate(zs) if i%2!=0]
				ycoords.sort()
				xcenter = 0
				ycenter = 0
				for i in range(len(xcoords)):
					xcenter = xcenter  + xcoords[i]
				for i in range(len(ycoords)):
					ycenter = ycenter  + ycoords[i]
				centroid = ((int(xcenter/len(xcoords))), int(ycenter/len(ycoords)))
				if len(approx) == 3: 
					shapeName = 'Triangle'
				elif len(approx) == 4: 
					p1x = approx.ravel()[0]
					p1y = approx.ravel()[1]
					p2x = approx.ravel()[2]
					p2y = approx.ravel()[3]
					p3x = approx.ravel()[4]
					p3y = approx.ravel()[5]
					d1 = ((p1x-p2x)**2 + (p1y-p2y)**2)**0.5
					d2 = ((p3x-p2x)**2 + (p3y-p2y)**2)**0.5
					if abs(d1 - d2) < 2:
						shapeName = 'Square'
					else: 
						shapeName = 'Rectangle'
				elif len(approx) == 5: 
					shapeName = 'Pentagon'
				detected_shapes.append([color, shapeName,  centroid])
	##################################################
	
	return detected_shapes

def get_labeled_image(img, detected_shapes):
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########
	"""
	Purpose:
	---
	This function takes the image and the detected shapes list as an argument
	and returns a labelled image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image

	Returns:
	---
	`img` :	[ numpy array ]
			labelled image
	
	Example call:
	---
	img = get_labeled_image(img, detected_shapes)
	"""
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########    

	for detected in detected_shapes:
		colour = detected[0]
		shape = detected[1]
		coordinates = detected[2]
		cv2.putText(img, str((colour, shape)),coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	return img

if __name__ == '__main__':
	
	# path directory of images in 'test_images' folder
	img_dir_path = 'test_images/'

	# path to 'test_image_1.png' image file
	file_num = 1
	img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
	
	# read image using opencv
	img = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor test_image_' + str(file_num) + '.png')
	
	# detect shape properties from image
	detected_shapes = detect_shapes(img)
	print(detected_shapes)
	
	# display image with labeled shapes
	img = get_labeled_image(img, detected_shapes)
	cv2.imshow("labeled_image", img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	
	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 16):
			
			# path to test image file
			img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
			
			# read image using opencv
			img = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor test_image_' + str(file_num) + '.png')
			
			# detect shape properties from image
			detected_shapes = detect_shapes(img)
			print(detected_shapes)
			
			# display image with labeled shapes
			img = get_labeled_image(img, detected_shapes)
			cv2.imshow("labeled_image", img)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()


