# opencv-api
##Description
Face-Detection using OpenCV library  with Django python server.

## Running Server:
Go to root directory of the project, and
```bash
$ python manage.py runserver
```

## POST request using `curl`:
* Posting image via URL:
```bash
$ curl -X POST 'http://localhost:8000/face_detection/detect/' -d 'url=https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg' ; echo ""
```
You will get response something like this,
```bash
{"num_faces": 1, "success": true, "faces": [[74, 54, 196, 176]]}
```
* Posting image  via file instead of URL:
```bash
$ curl -X POST -F image=@myimage.png 'http://localhost:8000/face_detection/detect/' ; echo ""
```
Here your response depends on your input image.
```bash
{"num_faces": 2, "success": true, "faces": [[88, 75, 179, 166], [216, 79, 301, 164]]}
```

##  Using cv-api via python code:
* In your *access_cv_api/* directory of the project, run the file **test_api**,
```bash
$ python test_api.py
```
Here, we have the code for both getting image via **URL** and **file** (from local storage). Just uncomment whatever you want.