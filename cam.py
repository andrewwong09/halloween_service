import cv2
import time
import os
from datetime import datetime
import numpy as np
from multiprocessing import Process


import motor_run as mr 


cache_dir = '/home/andrew/cache'

cam = cv2.VideoCapture(0)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

hits = 0
initial_state = None


def detect_human(frame):
    global hits
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    
    if len(boxes) > 0:
        hits = hits + 1
        
        now = datetime.now() # current date and time
        date_time = now.strftime("%m%d%Y_%H%M%S")
        cv2.imwrite(f"{os.path.join(cache_dir, date_time)}_0.png", frame.astype('uint8'))
        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)
        cv2.imwrite(f"{os.path.join(cache_dir, date_time)}_{len(boxes)}.png", frame.astype('uint8'))
    else:
        hits = 0
    
    if hits > 2:
        print(f"{date_time}_Hits: {hits}, Boxes found: {len(boxes)}")
        mr.run_motor(4)
        hits = 0


def detect_motion(frame):
    global initial_state
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)

    if initial_state is None:
        initial_state = gray_frame
        return

    now = datetime.now() # current date and time
    date_time = now.strftime("%m%d%Y_%H%M%S")

    differ_frame = cv2.absdiff(initial_state, gray_frame)
    
    # the change between static or initial background and current gray frame are highlighted 
    thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # For the moving object in the frame finding the coutours 
    cont, _ = cv2.findContours(thresh_frame.copy(),
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
    num_moving_obj = 0
    for cur in cont:
        if cv2.contourArea(cur) < 10000:
            continue
        num_moving_obj += 1
        (cur_x, cur_y, cur_w, cur_h) = cv2.boundingRect(cur)

        # To create a rectangle of green color around the moving object  
        cv2.rectangle(frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 255, 0), 3)

    if num_moving_obj > 0:
        print(f"{date_time}: Found {num_moving_obj} moving objects")
        p = Process(target=mr.run_motor)
        p.start()
        cv2.imwrite(f"{os.path.join(cache_dir, date_time)}_5.jpg", 
                    frame.astype('uint8'))

def start():
    global initial_state
    count = 0
    while(1):
        return_val, image = cam.read()
        #resized_img = cv2.resize(image, (640, 480))
        #rot_image = cv2.rotate(resized_img, cv2.ROTATE_90_CLOCKWISE)
        #detect_human(resized_img)
        if count == 10:
            initial_state = None
            count = 0
        rot_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        detect_motion(rot_image)

        time.sleep(0.1)
        count = count + 1
    cam.release()
