
from detection import *
from operator import itemgetter
import pyautogui
import sys
import time
class squabbler:
    row = 0
    def __init__(self):
        self.second_box = find_empty()
        self.first_box = find_cursor()

        print(self.first_box)
        print(self.second_box)
        assert(self.first_box != None, "could not find cursor. try resizing window?")
        assert(self.second_box != None, "could not find second empty box. try resizing window?")
        self.start_test_point = get_box_colour_region(self.first_box)
        self.box_distance = self.second_box.left - self.first_box.left
        self.word_list_file = open(sys.path[0] + "/../wordsv2.txt")
        self.full_word_list = self.word_list_file.readlines() 
        self.word_list = self.full_word_list[:]
        
        self.letter_count = [0] * 26
        self.used_letters = []
        self.ranked_word_list = []
        for word in self.full_word_list:
            self.ranked_word_list.append([word, 0])
    
    def check_row(self, row):
        """
        check the row specified for guess results
        """
        result = [None] * 5
        x_pos = self.start_test_point[0]
        y_pos = self.start_test_point[1] + row * self.box_distance
        for i in range(5):
            #print(x_pos)
            #pyautogui.moveTo(x_pos, y_pos, 0.15)
            if(test_yellow(x_pos, y_pos)):
                result[i] = "y"
            if(test_green(x_pos, y_pos)):
                result[i] = "g"
            x_pos += self.box_distance
        return result

    def check_row_empty(self, row):
        """
        checks if a row is empty
        """
        x_pos = self.start_test_point[0]
        y_pos = self.start_test_point[1] + row * self.box_distance
        return test_empty(x_pos, y_pos)

    def reset_word_list(self):
        """
        resets internal word list to the full list
        """
        self.word_list = self.full_word_list[:]
        self.used_letters.clear()

    def type_word(self, word):
        pyautogui.typewrite(word, 0.07)
        #time.sleep(0.3)
        pyautogui.press('enter') #just to make sure

    def eliminate_word(self, word, result):
        """
        eliminates words that are not possible from internal word list
        """
        to_remove = [] #workaround to avoid iterator funkiness
        #because iterator will screw up ordering
        #and skip over some elements if we were to delete them
        #while iterating
        for i in range(5):
            for w in self.word_list:
                if(result[i] == "y"):
                    if(word[i] not in w):
                        to_remove.append(w)
                        continue
                        
                    if(word[i] == w[i]):
                        to_remove.append(w)
                        continue
                    continue
                        
                if(result[i] == "g"):
                    if(word[i] != w[i]):
                        to_remove.append(w)
                        continue
                    continue
            for r in to_remove:
                self.word_list.remove(r)
                to_remove = []
        for letter in word:
            self.used_letters.append(letter)

    def guess_word(self):
        """
        guesses most optimal word
        the frequency of letters in the remaining words is counted
        and the words in the full word list are ranked accordingly
        """
        #first we start by counting
        for word in self.word_list:
            for letter in word:
                #letter = letter.lower()
                if letter == '\n':
                    break
                #print(ord(letter) - ord('A'))
                self.letter_count[ord(letter) - ord('A')] += 1
        #then we start assigning scores
        for word in self.ranked_word_list:
            for letter in word[0]: #index 0 is the actual word
                #we don't want to count letters that have already been guessed
                #since they are not very useful
                if letter == '\n':
                    break
                if letter not in self.used_letters:
                    word[1] += self.letter_count[ord(letter) - ord('A')] #index 1 is the score
        #and now we sort!
        self.ranked_word_list.sort(key=itemgetter(1), reverse=True)
        #and our final guess will be the first in the list
        return self.ranked_word_list[0]

    def reset_guess(self):
        """
        cleanup guess things
        """
        self.letter_count = [0] * 26

        self.ranked_word_list.clear()
        for word in self.full_word_list:
            self.ranked_word_list.append([word, 0])
                        


        


sq = squabbler()
time.sleep(2)

while(1):
    print("--------new word!--------")
    sq.reset_word_list()
    row = 0
    #guess 1
    guess = sq.guess_word()
    print(guess)
    sq.type_word(guess[0])
    while(not sq.check_row_empty(0)):    
        print("guesing "+guess[0])    
        result = sq.check_row(row)
        print("result for guess "+guess[0]+":"+str(result))
        sq.eliminate_word(guess[0], result)
        sq.reset_guess()
        time.sleep(0.25)
        guess = sq.guess_word()
        print(guess)
        sq.type_word(guess[0])
        row += 1
    print("done with word \n")
    """
    for g in initial_guess:

        sq.type_word(g)
        time.sleep(0.25)
        if(sq.check_row_empty(0)):
            #likely guessed correctly
            break
        print(g)
        result = sq.check_row(0)
        print(result)
        sq.eliminate_word(g, result)
        row += 1


    #guess 5
    sq.type_word(sq.word_list[0])
    print("guess 5 "+ sq.word_list[0])
    result = sq.check_row(0)
    print(result)
    sq.eliminate_word(sq.word_list[0], result)
    sq.word_list.remove(sq.word_list[0])
    if(sq.check_row_empty(0)):
        continue
    row += 1

    #guess 6
    try:
        sq.type_word(sq.word_list[0])
        print("guess 6 "+ sq.word_list[0])
        result = sq.check_row(row)
        print(result)
        sq.eliminate_word(sq.word_list[0], result)
        time.sleep(1)
    except:
        pass
    """



"""
#print(sq.check_row(-1))
#sq.word_list = ["apple", "pears", "poops", "flank"]
sq.eliminate_word("pksaa", ['g','y',None,None,None])
print(sq.word_list)
print(["g"]*5)
"""