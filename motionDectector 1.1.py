import cv2
import numpy as np
from twilio.rest import Client
from tkinter import *
import winsound

client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')


def motion_run():
    capture = cv2.VideoCapture(0)
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

        if frameCount > 500 and count > 5000:
            client.messages.create(to='+19786976468', from_='+19782952654',
                                   body='Motion Detected')
            frameCount = 0

        cv2.imshow('Frame', resizedFrame)
        cv2.imshow('Mask', fgmask)

        k = cv2.waitKey(5) & 0xff
        if k == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


top = Tk()
top.title('Salty Inc. Security')
top.geometry("270x30")
L1 = Label(top, text="Activation Code")
L1.pack(side=LEFT)
E1 = Entry(top, show="$", bd=5)
E1.pack(side=RIGHT)
E1.focus()


def check_val():
    if E1.get() == 'cabinVT!1':
        top.destroy()
        motion_run()
    else:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


submit_btn = Button(top, text="Submit", width=10, command=check_val)
submit_btn.pack(side=RIGHT)
top.mainloop()



