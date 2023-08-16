import pywhatkit
import time
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def sendMessageSchedule(number, message, hour, minute):
    pywhatkit.sendwhatmsg(number, message, hour, minute,10, True, 2)
    #pywhatkit.sendwhats_image(number, "/Users/JIAJUNKK_1/Desktop/PythonProjects/whatsappBot/image1.jpeg", True, 2)
    time.sleep(2)
    
    pyautogui.click()
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


"""
def sendImage(number):
    pywhatkit.sendwhats_image(number, "/Users/JIAJUNKK_1/Desktop/PythonProjects/whatsappBot/image1.jpeg")
    time.sleep(5)
    
    pyautogui.click()
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
"""


phoneNum = "Target's Phone Number"
message = "Your Message"


timeHour = #Hours in 24Hour System
timeMin =  #Minutes in 24Hour System
while True:
    timeMin += #Minutes per Period
    """
    if sending message every 15 minutes, timeMin += 15
    if sending message every 30 minutes, timeMin += 30
    """
    if timeMin % 60 != 0:
        sendMessageSchedule(phoneNum, message, timeHour, timeMin % 60)
        #sendImage(phoneNum)
    elif timeMin % 60 == 0:
        timeHour += 1
        if timeHour == 24:
            hour = 0
        sendMessageSchedule(phoneNum, message, timeHour, timeMin % 60)
        #sendImage(phoneNum)
    print("sent")











    





