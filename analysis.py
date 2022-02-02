import time
import matplotlib.pyplot as plt 
from words_by_frequency import freq as frequent_words
from words import words


letters = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}
others= 0
def get_proportions(dict):
    #get total count
    total = 0
    new_dict = {}
    for i in dict:
        total += dict[i]
    for i in dict:
        new_dict[i] =  dict[i] / total
    return new_dict
def get_histogram(dict, name):
    plt.bar(list(dict.keys()), dict.values(), color='r')
    plt.title(count)
    plt.savefig(f"{count}.png")

def get_sorted_letters(dict): #returns a list of tuples where 0:key 1:value
    list = [(k, v) for k, v in dict.items()] #to tuple list
    list.sort(key=lambda tup: tup[1], reverse=True)
    ret = []
    for i in list:
        ret.append(i[0])
    return ret

count = 0
for word in frequent_words:
    #count += 1
    #if (count % 500) == 0:
    #    print(get_sorted_letters(get_proportions(letters)), '\n')
    for letter in word:
        try: 
            letters[letter] += 1
        except:
            others += 1

def get_word_with_letters(letters, n):
    def reset_dict():
        for i in letter_status:
                    letter_status[i] = False
    word_list = []
    count = 0
    letter_status = {}
    for i in letters:
        letter_status[i] = False
    for word in words:
        reset_dict()
        for letter in word:
            if letter in letters:
                letter_status[letter] = True
        if False not in letter_status.values():
           word_list.append(word)
           count +=1
           if count>=n:
                break
    return word_list


#print(get_sorted_letters(get_proportions(letters)))