from words_by_frequency import freq as frequent_words
from words import words

latin_letters = 'qwertyuiopasdfghjklzxcvbnm'
def get_word_with_letters(letters, search_space=words):
    if letters == '':
        return search_space
    def reset_dict():
        for i in letter_status:
                    letter_status[i] = False
    word_list = []
    letter_status = {}
    for i in letters:
        letter_status[i] = False
    for word in search_space:
        reset_dict()
        for letter in word:
            if letter in letters:
                letter_status[letter] = True
        if False not in letter_status.values():
           word_list.append(word)
    return word_list
def filter(yellows, greens, greys, search_space=words):
    good_letters = [item for sublist in yellows for item in sublist] + [item for sublist in greens for item in sublist]
    possibilities = get_word_with_letters(''.join(good_letters), search_space)

    def filter_yellows(x):
        for count, i in enumerate(yellows):
            if x[count] in i:
                return False
        return True
    def filter_greens(x):
        for count, i in enumerate(greens):
            if i != [] and x[count] not in i:
                return False
        return True
    def filter_bad_letters():
        for i in word:
            if i in greys:
                return False
        return True
    filtered = []
    for word in possibilities:
        if filter_greens(word) and filter_yellows(word) and filter_bad_letters():
            filtered.append(word)
    return filtered
def get_most_popular(candidates, n=1, search_space=frequent_words):
    list = []
    count = 0
    for i in search_space:
        if i in candidates:
            list.append(i)
            if count >= n:
                return list
    if len(list) > 0:
        return list
    return False
def game(n=5):
    def play(str): #TODO: UX is terrible
        print('play ' + str)
        for i in range(n):
            y = input(f'yellow at pos {i}: ')
            g = input(f'green at pos {i}: ')
            if len(y) == 1 and y.lower() in latin_letters:
                yellows[i] = y
            if len(g) == 1 and g.lower() in latin_letters:
                greens[i] = g
        good_letters = [item for sublist in yellows for item in sublist] + [item for sublist in greens for item in sublist]
        for i in str:
            if i not in good_letters:
                greys.append(i)
    def loop():
        while True:
            filtered = filter(yellows, greens, greys)
            word_options = get_most_popular(filtered, 5)
            if word_options:
                print(f'Most common words are {word_options}.') 
                while True:
                    user_choice = input('Type the word you want to choose')
                    if user_choice in word_options:
                        break
                    print('wrong, try again')
                play(user_choice)
    gameRunning: True
    yellows = []
    greens =  []
    greys = []
    for i in range(n):
        yellows.append([])
        greens.append([])
    #TODO: code for n != 5
    play('aeros')
    loop()

game()