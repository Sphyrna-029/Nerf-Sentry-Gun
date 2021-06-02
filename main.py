######################
# Made by MilkJug
# Last Updated on: 6/2/2021
# Repo Forked From BuckarewBanzai
# Uses OpenCV
#
######################

import cv2

# Source data : Video File
IP_file = 'Road3.mp4'

# Read the source video file
vid_file = cv2.VideoCapture(IP_file)

# pre trained classifiers
cup_classifier = 'cup.xml'
human_classifier = 'human.xml'



# Classified Trackers
cup_tracker = cv2.CascadeClassifier(car_classifier)
human_tracker = cv2.CascadeClassifier(human_classifier)


while True:
    # start reading video file frame by frame like an image
    (read_successful, frame) = vid_file.read()

    if read_successful:
        #convert to grey scale image
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Cars, Pedestrians, Bus and 2Wheelers
    cup = cup_tracker.detectMultiScale(gray_frame,1.1,9)
    human = human_tracker.detectMultiScale(gray_frame,1.1,9)
   

    # Draw rectangle around the cars
    for (x, y, w, h) in cup:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, 'Cup', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        #cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Draw square around the pedestrians
    for (x, y, w, h) in human:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Human', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # display the imapge with the face spotted
    cv2.imshow('Detect Objects ',frame)

    # capture key
    key = cv2.waitKey(1)

    # Stop incase Esc is pressed
    if key == 27:
        break

# Release video capture object
vid_file.release()

print("That's it...")
