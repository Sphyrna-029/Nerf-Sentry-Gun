# import the opencv library
import cv2


# Source data
img_file = "C:\\Users\Milk\\Documents\\program\\person.jpeg"

# create an openCV image 
img = cv2.imread(img_file)

person_classifier = "C:\\Users\\Milk\\Documents\\program\\haarcascade_person.xml"
# cup_classifier = 'file_name.xml' if you can find a cup.xml file

# convert color image to grey image '
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create trackers using classifiers using OpenCV
person_tracker = (cv2.data.haarcascades + person_classifier)
# cup_tracker = cv2.CascadeClassifier(cup_classifier)

# detect objects
person = person_tracker.detectMultiScale(gray_img)
# cup = cup_tracker.detectMultiScale(gray_img)

# Display the coordinates of different objects - multi dimensional array   
print(person)

# draw rectangles around the objects.
for (x, y, w, h) in person:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, 'Person', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255,0), 2)
# Just copy this blerb of code above and change the 2 'person' tags to a different object
cv2.imshow('my dection', img)

# wait for the keystroke to exit before
cv2.waitKey()


