import cv2
import numpy as np
from twilio.rest import Client


capture = cv2.VideoCapture(0)

client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')

fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, True)

frameCount = 0

while 1:

    ret, frame = capture.read()

    if not ret:
        break

    frameCount += 1

    resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

    fgmask = fgbg.apply(resizedFrame)

    count = np.count_nonzero(fgmask)

    print('Frame: %d, Pixel Count: %d' % (frameCount, count))

    if frameCount > 1 and count > 5000:
        client.messages.create(to='+19786976468', from_='+19782952654',
                               body='Motion Detected')

    cv2.imshow('Frame', resizedFrame)
    cv2.imshow('Mask', fgmask)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
