import pyautogui
import sys

def test_detection():
    """
    test to see if script can detect letters & colours correctly
    requires opencv
    """
    currdir = sys.path[0]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        out = char+": "
        if(pyautogui.locateOnScreen(currdir + "/charimgs/"+char+"_yellow.png", grayscale=False, confidence=0.88)):
            out += "Y"
        if(pyautogui.locateOnScreen(currdir + "/charimgs/"+char+"_green.png", grayscale=False, confidence=0.88)):
            out += "G"
        print(out)
    #number of empty cells is always fewer by 1 as the script does not detect the cell the cursor is on
    print(len(list(pyautogui.locateAllOnScreen(currdir+"/empty.png", grayscale=False, confidence=0.9))))

test_detection()