# opencv-api
##Description
Face-Detection using OpenCV library  with Django python server.

## Running Server:
Go to root directory of the project, and
```bash
$ python manage.py runserver
```

## POST request using `curl`:
```bash
$ curl -X POST 'http://localhost:8000/face_detection/detect/' -d 'url=https://lh6.googleusercontent.com/-zL2hGAaDwmU/AAAAAAAAAAI/AAAAAAAC4-o/4p4uf0mnPDs/s0-c-k-no-ns/photo.jpg'
```
You will get something like this,
```bash
{"num_faces": 1, "success": true, "faces": [[102, 64, 311, 273]]}
```
