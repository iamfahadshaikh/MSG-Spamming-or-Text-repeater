import pyautogui as spam
import time
import sys
 
def spamming(limit,msg):
    i = 0
    time.sleep(5)
    while(i<int(limit)):
        spam.typewrite(msg)
        spam.press("Enter")
        i+= 1
        # time.sleep()

if __name__ =='__main__':
    if (len(sys.argv) <3):
        limit = input("Enter message count : ")
        msg = input("Message you want to send : ")
    elif (len(sys.argv) != 3):
        print(len(sys.argv),sys.argv)
        print("python spammer.py `count` `msg` \n")
        exit()
    else:
        limit = sys.argv[1]
        msg = sys.argv[2]
     
    spamming(limit,msg)