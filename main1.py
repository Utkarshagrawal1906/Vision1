import cv2
from simple_facerec import SimpleFacerec
sfr=SimpleFacerec()
def img():
    sfr.load_encoding_images("images/")

def face():
    cap=cv2.VideoCapture(0)
    while True:
        ret, frame=cap.read()
        fls,fn=sfr.detect_known_faces(frame)
        for fl,n in zip(fls,fn):
            y1,x1,y2,x2=fl[0],fl[1],fl[2],fl[3]
            cv2.putText(frame, n, (x2, y1-10),cv2.FONT_HERSHEY_DUPLEX,0.7,(0,0,0),2)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),4)
        cv2.imshow("Frame",frame)
        if len(fn)>0:
            cap.release()
            cv2.destroyAllWindows()
            return fn[0]