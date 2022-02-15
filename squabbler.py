from detection import *
import time
class squabbler:
    row = 0
    def __init__(self):
        self.second_box = find_empty()
        self.first_box = find_cursor()

        print(self.first_box)
        print(self.second_box)
        #assert(self.first_box != None, "could not find cursor. try resizing window?")
        #assert(self.second_box != None, "could not find second empty box. try resizing window?")
        self.start_test_point = get_box_colour_region(self.first_box)
        self.box_distance = self.second_box.left - self.first_box.left
    
    def check_row(self, row):
        result = [None] * 5
        x_pos = self.start_test_point[0]
        y_pos = self.start_test_point[1] + row * self.box_distance
        for i in range(5):
            print(x_pos)
            pyautogui.moveTo(x_pos, y_pos, 1)
            if(test_yellow(x_pos, y_pos)):
                result[i] = "y"
            if(test_green(x_pos, y_pos)):
                result[i] = "g"
            x_pos += self.box_distance
        return result

sq = squabbler()
print(sq.check_row(-1))
