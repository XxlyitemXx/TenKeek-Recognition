import cv2

name = LekTheRat

cam = cv2.VideoCapture(0)

cv2.namedWindow("[**เล็ก**] กด space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("[**เล็ก**] กด space to take a photo", 500, 300)

img_counter = 0

while true: 
    ret, frame = cam.read()
    if not ret:
        print("[**เล็ก** ]failed to grab frame")
        break
    cv2.imshow("[**เล็ก**] press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("[**เล็ก**] Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()




cv2.destroyAllWindows()

