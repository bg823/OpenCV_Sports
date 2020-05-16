"""
Mouse as a Paint-Brush in OpenCV
reference site : https://docs.opencv.org/4.2.0/db/d5b/tutorial_py_mouse_handling.html
"""
import cv2 as cv
import pprint

events = [i for i in dir(cv) if 'EVENT' in i]
pprint.pprint(events)
