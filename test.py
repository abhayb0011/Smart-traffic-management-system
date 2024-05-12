import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model=YOLO('best.pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('Smart traffic management system')
cv2.setMouseCallback('Smart traffic management system', RGB)
            
        



cap=cv2.VideoCapture('video3.mp4')


my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)



count=0
area1=[(509,308),(567,308),(594,499),(509,499)]
area2=[(437,292),(0,289),(0,257),(441,260)]
area3=[(512,216),(454,214),(476,29),(509,22)]
area4=[(1019,222),(1019,259),(579,255),(592,229)]


while True:    
    ret,frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
   

#    print(px)
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        cx=int(x1+x2)//2
        cy=int(y1+y2)//2
        w,h=x2-x1,y2-y1

        #for area1 detection:
        result1=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
        if result1>=0:
    #       cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
            cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
            cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
            #cvzone.putTextRect(frame,f'vehicle',(x1,y1),1,1)
            list1.append(cx)
        
        #for area2 detection:
        result2=cv2.pointPolygonTest(np.array(area2,np.int32),((cx,cy)),False)
        if result2>=0:
    #       cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
            cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
            cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
            #cvzone.putTextRect(frame,f'vehicle',(x1,y1),1,1)
            list2.append(cx)

        #for area3 detection:
        result3=cv2.pointPolygonTest(np.array(area3,np.int32),((cx,cy)),False)
        if result3>=0:
    #       cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
            cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
            cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
            #cvzone.putTextRect(frame,f'vehicle',(x1,y1),1,1)
            list3.append(cx)

        #for area4 detection:
        result4=cv2.pointPolygonTest(np.array(area4,np.int32),((cx,cy)),False)
        if result4>=0:
    #       cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),-1)
            cvzone.cornerRect(frame,(x1,y1,w,h),3,2)
            cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
            #cvzone.putTextRect(frame,f'vehicle',(x1,y1),1,1)
            list4.append(cx)
        
    cnt1=len(list1)
    cnt2=len(list2)
    cnt3=len(list3)
    cnt4=len(list4)
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,0,255),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,0,0),2)
    cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,255,0),2)
    cv2.polylines(frame,[np.array(area4,np.int32)],True,(255,255,0),2)
    cvzone.putTextRect(frame,f'South:-{cnt1}',(771,402),1,1)
    cvzone.putTextRect(frame,f'West:-{cnt2}',(95,395),1,1)
    cvzone.putTextRect(frame,f'North:-{cnt3}',(182,76),1,1)
    cvzone.putTextRect(frame,f'East:-{cnt4}',(737,77),1,1)

    cv2.imshow("Smart traffic management system", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()


