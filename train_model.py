import imutils 
import paths
import face_recognition
import pickle
import cv2
import os

print("[INFO][**เล็ก**]  เล็กกำลังโหลดจ้าา")
imagePaths = list(paths.list_images("dataset"))

knownEncodings = []
knownNames = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	
	print("[INFO][**เล็ก**]  เล็กกำลังทำ :D {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]


image = cv2.imread(imagePath)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

boxes = face_recognition.face_location(rgb,
model="hog")

encodings = face_recognition.face_encodings(rgb,boxes)

for encoding in encoding:
	knownEncodings.append(encoding)
	knownNames.append(name)
	
print("[INFO] [**เล็ก**] เสร็จแล้วหัดรอบ้างนะไอสัส")
data =  {"encoding": knownEncodings, "name": knownNames}
f = open("encoding.pickel", "wb")
f.write(pickle.dump(data))
f.close()