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
        if(pyautogui.locateOnScreen(currdir + "/charimgs/"+char+"_yellow.png", grayscale=False, confidence=0.85)):
            out += "Y"
        if(pyautogui.locateOnScreen(currdir + "/charimgs/"+char+"_green.png", grayscale=False, confidence=0.85)):
            out += "G"
        print(out)
    #number of empty cells is always fewer by 1 as the script does not detect the cell the cursor is on
    print(len(list(pyautogui.locateAllOnScreen(currdir+"/empty.png", grayscale=False, confidence=0.9))))

def find_cursor():
    """
    finds the current letter cursor
    """
    currdir = sys.path[0]
    return pyautogui.locateOnScreen(currdir + "/cursor.png", grayscale = False, confidence = 0.75)


def find_empty():
    """
    finds the first empty box
    """
    currdir = sys.path[0]
    return pyautogui.locateOnScreen(currdir + "/empty.png", grayscale = False, confidence = 0.75)

def get_box_colour_region(box):
    return (box.left + int(box.width*0.2), box.top + int(box.height*0.2))
def test_yellow(x, y):
    return pyautogui.pixelMatchesColor(int(x), int(y), (214, 190, 0), tolerance=10)
def test_green(x, y):
    return pyautogui.pixelMatchesColor(int(x), int(y), (46, 216, 60), tolerance=10)
def test_empty(x, y):
    return pyautogui.pixelMatchesColor(int(x), int(y), (167, 113, 248), tolerance=1)
def get_length_diff():
    cursor = find_cursor().left
    empty = find_empty().left
    return empty-cursor
#green : 2ED83C aka 46, 216, 60
#yellow: D6BE00 aka 214, 190, 0

"""
#for i in range(5):
#    test_yellow()
currdir = sys.path[0]
print(pyautogui.locateOnScreen(currdir + "/empty.png", grayscale = False, confidence=0.75))
print(pyautogui.locateOnScreen(currdir + "/cursor.png", grayscale = False, confidence=0.75))
#pyautogui.moveTo(get_box_colour_region(find_cursor())[0], get_box_colour_region(find_cursor())[1])
"""