from ntpath import join
from english_words import english_words_lower_alpha_set
import random

def choose():
    word_list = []
    for words in english_words_lower_alpha_set:
        word_list.append(words)
    return random.choice(word_list)

def jumble(word):
    return ''.join(random.sample(word, len(word)))

def play():
    p1name=input('Player 1, please enter your name: ')
    p2name=input('Player 2, please enter your name: ')
    p1_points = 0
    p2_points = 0
    turn = 0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        while(qn==picked_word):
            qn=jumble(picked_word)
        
        print('Your word is: {}'.format(qn))
        if turn%2==0:
            print('{}\'s Turn'.format(p1name))
            ans=input('Enter your answer: ')
            if ans == picked_word:
                p1_points += 1
                print('Thats the right ans!')
            else:
                print('No you son of a bitch!\nThe correct word is this: {}'.format(picked_word))
        
        if turn%2!=0:
            print('{}\'s Turn'.format(p2name))
            ans=input('Enter your answer: ')
            if ans == picked_word:
                p2_points += 1
                print('Thats the right ans!')
            else:
                print('No you son of a bitch!\nThe correct word is: {}'.format(picked_word))
            print('Here are the scores so far\n{}: {} points\n{}: {} points'.format(p1name, p1_points, p2name, p2_points))
            choice = input('Enter \'Y\' to continue playing or \'N\' to stop playing: ')
            if choice.lower() == 'n':
                break
        
        turn+=1

play()
