# import the necessary packages
import requests
import cv2
from url_to_image import url_to_image
 
# define the URL to our face detection API
api_url = "http://localhost:8000/face_detection/detect/"
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg"
 
# use our face detection API to find faces in images via image URL
image = url_to_image(image_url)
payload = {"url": image_url}
r = requests.post(api_url, data=payload).json()

# OR load our image and now use the face detection API to find faces in
# images by uploading an image directly
#
# image = cv2.imread("images/PM_Modi_2015.jpg")
# payload = {"image": open("images/PM_Modi_2015.jpg", "rb")}
# r = requests.post(api_url, files=payload).json()

print "PM_Modi_2015.jpg: {}".format(r)
 
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
# show the output image
cv2.imshow("PM_Modi_2015.jpg", image)
cv2.waitKey(0)